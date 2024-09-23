with open("packages.txt", "r") as f_in, open("requirements.txt", "w") as f_out:
    for line in f_in.readlines()[2:]:  # Пропускаем первые 2 строки (заголовки таблицы)
        package, version = line.split()[:2]
        f_out.write(f"{package}=={version}\n")
