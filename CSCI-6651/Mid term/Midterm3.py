def main():
    start = 0.0
    end = 100.0
    step = 0.1
    num_point = int((end - start)/step) +1

    points = [(round(start + i * step, 2), round((start + i * step)**2 ,2)) for i in range(num_point)]

    print(f"{'point #': >7} {'x': >7} {'y': >10}")

    for idx, (x,y) in enumerate(points, start=1):
        print(f"{idx:7d} {x:7.2f} {y:10.2f}")


if __name__ == "__main__":
    main()