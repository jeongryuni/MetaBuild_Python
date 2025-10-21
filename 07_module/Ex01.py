from Tools.scripts.summarize_stats import emit_execution_counts


def abc():
    print("abc")

def xyz():
    print("xyz")

# 현재 파일(main)에서만 실행할때 abc호출
print("__name__:", __name__)
if __name__=="__main__":
    abc()

