import conducto as co


def test() -> co.Serial:
    output = co.Serial()
    output["node1"] = co.Exec("echo testing")
    return output


if __name__ == "__main__":
    #co.Image.share_directory("GRADED_HACK", ".")

    co.main()
