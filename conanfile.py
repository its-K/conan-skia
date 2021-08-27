from conans import ConanFile, CMake
import os

def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

class HelloConan(ConanFile):
    name = "skia"
    version = "1.0"
    license = "MIT License"
    email = "kishore4110@gmail.com"
    url = "https://github.com/its-k/conan-skia"
    description = "Skia is a complete 2D graphic library for drawing Text, Geometries, and Images."
    topics = ("render", "vector", "2d", "3d")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    exports_sources = "skia/*","headerChange.py"

    skia_options = {
        "skia_build_fuzzers" : [True,False],
        "skia_compile_processors" : [True,False],
        "skia_compile_sksl_tests" : [True,False],
        "skia_enable_android_utils" : [True,False],
        "skia_enable_api_available_macro" : [True,False],
        "skia_enable_direct3d_debug_layer" : [True,False],
        "skia_enable_discrete_gpu" : [True,False],
        "skia_enable_flutter_defines" : [True,False],
        "skia_enable_fontmgr_android" : [True,False],
        "skia_enable_fontmgr_custom_directory" : [True,False],
        "skia_enable_fontmgr_custom_embedded" : [True,False],
        "skia_enable_fontmgr_custom_empty" : [True,False],
        "skia_enable_fontmgr_empty" : [True,False],
        "skia_enable_fontmgr_fontconfig" : [True,False],
        "skia_enable_fontmgr_fuchsia" : [True,False],
        "skia_enable_fontmgr_win" : [True,False],
        "skia_enable_fontmgr_win_gdi" : [True,False],
        "skia_enable_gpu" : [True,False],
        "skia_enable_gpu_debug_layers" : [True,False],
        "skia_enable_metal_debug_info" : [True,False],
        "skia_enable_particles" : [True,False],
        "skia_enable_pdf" : [True,False],
        "skia_enable_skgpu_v1" : [True,False],
        "skia_enable_skgpu_v2" : [True,False],
        "skia_enable_skottie" : [True,False],
        "skia_enable_skparagraph" : [True,False],
        "skia_enable_skrive" : [True,False],
        "skia_enable_skshaper" : [True,False],
        "skia_enable_sksl" : [True,False],
        "skia_enable_sktext" : [True,False],
        "skia_enable_skvm_jit_when_possible" : [True,False],
        "skia_enable_spirv_validation" : [True,False],
        "skia_enable_svg" : [True,False],
        "skia_enable_tools" : [True,False],
        "skia_enable_vulkan_debug_layers" : [True,False],
        "skia_enable_winuwp" : [True,False],
        "skia_generate_workarounds" : [True,False],
        "skia_include_multiframe_procs" : [True,False],
        "skia_lex" : [True,False],
        "skia_pdf_subset_harfbuzz" : [True,False],
        "skia_tools_require_resources" : [True,False],
        "skia_update_fuchsia_sdk" : [True,False],
        "skia_use_angle" : [True,False],
        "skia_use_dawn" : [True,False],
        "skia_use_direct3d" : [True,False],
        "skia_use_dng_sdk" : [True,False],
        "skia_use_egl" : [True,False],
        "skia_use_expat" : [True,False],
        "skia_use_experimental_xform" : [True,False],
        "skia_use_ffmpeg" : [True,False],
        "skia_use_fixed_gamma_text" : [True,False],
        "skia_use_fontconfig" : [True,False],
        "skia_use_fonthost_mac" : [True,False],
        "skia_use_freetype" : [True,False],
        "skia_use_freetype_woff2" : [True,False],
        "skia_use_gl" : [True,False],
        "skia_use_harfbuzz" : [True,False],
        "skia_use_icu" : [True,False],
        "skia_use_libfuzzer_defaults" : [True,False],
        "skia_use_libgifcodec" : [True,False],
        "skia_use_libheif" : [True,False],
        "skia_use_libjpeg_turbo_decode" : [True,False],
        "skia_use_libjpeg_turbo_encode" : [True,False],
        "skia_use_libpng_decode" : [True,False],
        "skia_use_libpng_encode" : [True,False],
        "skia_use_libwebp_decode" : [True,False],
        "skia_use_libwebp_encode" : [True,False],
        "skia_use_lua" : [True,False],
        "skia_use_metal" : [True,False],
        "skia_use_ndk_images" : [True,False],
        "skia_use_piex" : [True,False],
        "skia_use_runtime_icu" : [True,False],
        "skia_use_sfml" : [True,False],
        "skia_use_sfntly" : [True,False],
        "skia_use_system_expat" : [True,False],
        "skia_use_system_freetype2" : [True,False],
        "skia_use_system_harfbuzz" : [True,False],
        "skia_use_system_icu" : [True,False],
        "skia_use_system_libjpeg_turbo" : [True,False],
        "skia_use_system_libpng" : [True,False],
        "skia_use_system_libwebp" : [True,False],
        "skia_use_system_zlib" : [True,False],
        "skia_use_vma" : [True,False],
        "skia_use_vulkan" : [True,False],
        "skia_use_webgl" : [True,False],
        "skia_use_wuffs" : [True,False],
        "skia_use_x11" : [True,False],
        "skia_use_xps" : [True,False],
        "skia_use_zlib" : [True,False],
        "is_official_build" : [True,False]
    }

    options = merge_two_dicts({ "shared": [True, False] }, skia_options)

    default_options = {
        "shared":False,
        # Skia options
        "skia_build_fuzzers" : False,
        "skia_compile_processors" : False,
        "skia_compile_sksl_tests" : False,
        "skia_enable_android_utils" : False,
        "skia_enable_api_available_macro" : True,
        "skia_enable_direct3d_debug_layer" : False,
        "skia_enable_discrete_gpu" : False,
        "skia_enable_flutter_defines" : False,
        "skia_enable_fontmgr_android" : True,
        "skia_enable_fontmgr_custom_directory" : True,
        "skia_enable_fontmgr_custom_embedded" : True,
        "skia_enable_fontmgr_custom_empty" : True,
        "skia_enable_fontmgr_empty" : False,
        "skia_enable_fontmgr_fontconfig" : False,
        "skia_enable_fontmgr_fuchsia" : False,
        "skia_enable_fontmgr_win" : False,
        "skia_enable_fontmgr_win_gdi" : False,
        "skia_enable_gpu" : False,
        "skia_enable_gpu_debug_layers" : False,
        "skia_enable_metal_debug_info" : False,
        "skia_enable_particles" : True,
        "skia_enable_pdf" : False,
        "skia_enable_skgpu_v1" : True,
        "skia_enable_skgpu_v2" : False,
        "skia_enable_skottie" : True,
        "skia_enable_skparagraph" : True,
        "skia_enable_skrive" : True,
        "skia_enable_skshaper" : True,
        "skia_enable_sksl" : True,
        "skia_enable_sktext" : True,
        "skia_enable_skvm_jit_when_possible" : False,
        "skia_enable_spirv_validation" : False,
        "skia_enable_svg" : True,
        "skia_enable_tools" : False,
        "skia_enable_vulkan_debug_layers" : False,
        "skia_enable_winuwp" : False,
        "skia_generate_workarounds" : False,
        "skia_include_multiframe_procs" : False,
        "skia_lex" : False,
        "skia_pdf_subset_harfbuzz" : False,
        "skia_tools_require_resources" : False,
        "skia_update_fuchsia_sdk" : False,
        "skia_use_angle" : False,
        "skia_use_dawn" : False,
        "skia_use_direct3d" : False,
        "skia_use_dng_sdk" : True,
        "skia_use_egl" : False,
        "skia_use_expat" : True,
        "skia_use_experimental_xform" : False,
        "skia_use_ffmpeg" : False,
        "skia_use_fixed_gamma_text" : False,
        "skia_use_fontconfig" : False,
        "skia_use_fonthost_mac" : False,
        "skia_use_freetype" : True,
        "skia_use_freetype_woff2" : False,
        "skia_use_gl" : False,
        "skia_use_harfbuzz" : True,
        "skia_use_icu" : True,
        "skia_use_libfuzzer_defaults" : True,
        "skia_use_libgifcodec" : True,
        "skia_use_libheif" : False,
        "skia_use_libjpeg_turbo_decode" : True,
        "skia_use_libjpeg_turbo_encode" : True,
        "skia_use_libpng_decode" : True,
        "skia_use_libpng_encode" : True,
        "skia_use_libwebp_decode" : True,
        "skia_use_libwebp_encode" : True,
        "skia_use_lua" : False,
        "skia_use_metal" : False,
        "skia_use_ndk_images" : False,
        "skia_use_piex" : True,
        "skia_use_runtime_icu" : False,
        "skia_use_sfml" : False,
        "skia_use_sfntly" : True,
        "skia_use_system_expat" : True,
        "skia_use_system_freetype2" : True,
        "skia_use_system_harfbuzz" : False,
        "skia_use_system_icu" : True,
        "skia_use_system_libjpeg_turbo" : True,
        "skia_use_system_libpng" : True,
        "skia_use_system_libwebp" : True,
        "skia_use_system_zlib" : True,
        "skia_use_vma" : False,
        "skia_use_vulkan" : False,
        "skia_use_webgl" : False,
        "skia_use_wuffs" : False,
        "skia_use_x11" : True,
        "skia_use_xps" : True,
        "skia_use_zlib" : True,
        "is_official_build" : True
    }

    def source(self):
        #self.run("git clone https://skia.googlesource.com/skia.git")
        self.run("python2 skia/tools/git-sync-deps")

    def requirements(self):
        if self.options.skia_use_system_icu and self.options.skia_use_icu:
            self.requires("icu/69.1")
        self.requires("libwebp/1.2.0")
        self.requires("freetype/2.10.4")
        if self.options.skia_use_system_libjpeg_turbo:
            self.requires("libjpeg-turbo/1.5.2@bincrafters/stable")
        if self.options.skia_use_system_libpng:
            self.requires("libpng/1.6.36@bincrafters/stable")
    
    def configure(self):
        if self.settings.os == "Linux":
            print("Its Linux \n")

    def build(self):
        opts=[]
        for k,v in self.options.items():
            if k in self.skia_options:
                opts += [("%s=%s" % (k,v)).lower()]
        if len(opts) > 0:
            opts = '"--args=%s"' % " ".join(opts)
        else:
            opts = ""
        self.run('cd skia && bin/gn gen out/conan-build %s' %(opts))
        self.run("ninja -C skia/out/conan-build")
        #self.run("python3 headerChange.py")

    def package(self):
        self.copy("*.h", dst="include", src="skia", keep_path=True)
        self.copy("*.lib", dst="lib", src="skia/out/conan-build", keep_path=False)
        self.copy("*.dll", dst="bin", src="skia/out/conan-build", keep_path=False)
        self.copy("*.dylib*", dst="lib", src="skia/out/conan-build", keep_path=False)
        self.copy("*.so", dst="lib", src="skia/out/conan-build", keep_path=False)
        self.copy("*.a", dst="lib", src="skia/out/conan-build", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["skia"]
