def build_extension(self, ext):
    try:
        return super().build_extension(ext)
    except CompileError:
        if ext.extra_compile_args and '-maes' in ext.extra_compile_args:
            print("Failed to build; Compiling without AES-NI")
            ext.extra_compile_args.remove('-maes')
            ext.extra_compile_args.remove('-mpclmul')
            return super().build_extension(ext)
        else:
            raise
