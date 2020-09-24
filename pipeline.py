import conducto as co

def pr() -> co.Parallel:
    image = co.Image(copy_repo=True)
    output = co.Parallel()
    output["test"] = co.Exec("echo running the tests")
    return output

if __name__ == "__main__":
    co.main()
