from climage import (
        convert,
        color_to_flags,
        color_types
        )

class Logo:
    def __init__(self, image):
        self.image = image
        print(f"{self.run()}\n{'@_@' * 8}\n")

    def run(self) -> str:
        output = convert(
                self.image,
                is_unicode = True,
                width = 25,
                **color_to_flags(
                    color_types.truecolor
                    ),
                )
        return output


if __name__ == "__main__":
    Logo("app/frontend/assets/img/174.png")
