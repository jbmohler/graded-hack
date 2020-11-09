import conducto as co
import sympy


def factor(n):
    print(sympy.factorint(int(n)))


def test() -> co.Serial:
    image = co.Image(dockerfile="docker/Dockerfile", copy_repo=True)

    output = co.Serial(image=image)
    output["node1"] = co.Exec("echo testing")
    output["factor"] = co.Exec(factor, 91235)
    return output


if __name__ == "__main__":
    # co.Image.share_directory("GRADED_HACK", ".")

    co.main()
