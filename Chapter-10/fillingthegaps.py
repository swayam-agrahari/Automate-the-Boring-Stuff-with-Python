def FillingGaps(path):
    import re, os, shutil

    p1 = 0
    p2 = 0
    p3 = 1
    s1 = str(p1)
    s2 = str(p2)
    s3 = str(p3)

    preffix = "001"
    preffix_re = re.compile(r"(\d{3})(\.[a-z]{3,4})")

    for filename in os.listdir(path):
        mo = preffix_re.search(filename)
        try:
            if filename.endswith(mo.group()):
                if preffix == mo.group(1):
                    p3 += 1
                    s3 = str(p3)
                    print("good file: " + filename)
                    if s3[-1] == 0:
                        p2 += 1
                        s2 = str(p2)
                        if s2[-1] == 0:
                            p1 += 1
                            s1 = str(p1)
                            if s1[-1] == 0:
                                print("Max limit reached: 999")
                                break

                    preffix = s1[-1] + s2[-1] + s3[-1]

                else:
                    new_filename = preffix_re.sub(preffix + r"\2", filename)
                    print("New File: " + new_filename)
                    shutil.move(path / filename, path / new_filename)
                    p3 += 1
                    s3 = str(p3)
                    print(filename)
                    if s3[-1] == 0:
                        p2 += 1
                        s2 = str(p2)
                        if s2[-1] == 0:
                            p1 += 1
                            s1 = str(p1)
                            if s1[-1] == 0:
                                print("Max limit reached: 999")
                                break

                    preffix = s1[-1] + s2[-1] + s3[-1]

        except:
            continue

