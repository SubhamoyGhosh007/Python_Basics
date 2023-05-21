import os

# if not os.path.exists("garbage"):
#     os.mkdir("garbage")
# if not os.path.exists("garbage/data"):
#     os.mkdir("garbage/data")
#
# for i in range(0, 100):
#     if not os.path.exists(f"garbage/data/Day {i+1}"):
#         os.mkdir(f"garbage/data/Day {i+1}")
#     for j in range(0, 10):
#         if not os.path.exists(f"garbage/data/Day {i+1}/Tutorial {j+1}"):
#             os.mkdir(f"garbage/data/Day {i+1}/Tutorial {j+1}")
#
# for i in range(0, 100):
#     if not os.path.exists(f"garbage/data/Day{i+1}"):
#         continue
#     else:
#         os.rename(f"garbage/data/Day{i+1}", f"garbage/data/Day {i+1}")

# folders = os.listdir("garbage/data")
#
# for folder in folders:
#     print(folder)
#     print(os.listdir(f"garbage/data/{folder}"))

# print(os.getcwd())
# os.chdir("garbage/data")
# print(os.getcwd())
