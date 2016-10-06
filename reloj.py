def simuladorReloj():
    for h in range(1, 24):  # parar en 23
        for m in range(1, 60):  # parar en 59
            for s in range(1, 60):  # parar en 59
                print(str(h).zfill(2), ":", str(m).zfill(2), ":", str(s).zfill(2))

simuladorReloj()