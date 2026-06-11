from sys import argv

if __name__ == '__main__':
    print(argv)

    script = argv[1]

    # 根据传入参数，确定执行的脚本
    match script:
        case 'preprocess':
            from process.preprocess import preprocess
            preprocess()
        case 'train':
            from runner.train import train
            train()