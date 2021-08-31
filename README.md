## Conan package recipe for *skia*

Skia provides 2D / 3D Vector rendering

It builds only the library, without any demos or tools found in skia

## Issues

If you wish to report an issue or make a request for a package, please do so here:

[Issues Tracker](https://github.com/its-k/conan-skia/issues)


## For Users

### Basic setup

    conan create .

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    skia/1.0

    [generators]
    txt

Complete the installation of requirements for your project running:

    mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.

## Supported OS

Currenly this package works for and provides packages for MacOS and Linux. Pull Requests for other platforms are very welcome ( see [Issues Tracker](https://github.com/Maddimax/conan-skia/issues) )


## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache. This includes all necessary requirements

    # macOS
	$ conan create . -o skia:skia_use_metal=True --build missing
    # linux
    $ conan create . --build missing

NOTE: The conan recipe license applies only to the files of this recipe, which can be used to build and package skia.
It does *not* in any way apply or is related to the actual software being packaged.

[MIT](LICENSE)