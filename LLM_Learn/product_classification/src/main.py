# from sys import argv
from argparse import ArgumentParser

if __name__ == '__main__':
    # print(argv)
    #
    # script = argv[1]

    # 定义解析器
    parser = ArgumentParser(usage="usage: main.py action")
    parser.add_argument('action', choices=['preprocess','train','predict','evaluate','run_app'])

    # 解析参数
    action = parser.parse_args().action

    # 根据传入参数，确定执行的脚本
    match action:
        case 'preprocess':
            from process.preprocess import preprocess
            preprocess()
        case 'train':
            from runner.train import train
            train()
        case 'predict':
            from runner.predict import predict
            predict()
        case 'evaluate':
            from runner.evaluate import evaluate
            evaluate()
        case 'run_app':
            from web.web_app import run_app
            run_app()