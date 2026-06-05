from concurrent.futures import ProcessPoolExecutor
import multiprocessing
def send_message(conn):
    messages = [
        "哈哈",
        "呵呵",
        "嘻嘻",
        None
    ]

    conn.send(messages)

    message = conn.recv()
    print(message)


def recv_messsage(conn):
    data = conn.recv()
    print(data)

    conn.send("我爱你杨幂")



if __name__ == '__main__':

    conn1,conn2 = multiprocessing.Pipe()  #拿到管道的两个端点

    with ProcessPoolExecutor(max_workers=2) as executor:
        executor.submit(send_message,conn1)
        executor.submit(recv_messsage,conn2)


