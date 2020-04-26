from colorama import Back,Fore,Style

# print(Fore.LIGHTGREEN_EX,"hello world")
# print(Back.LIGHTBLUE_EX,"hello world")
# print(Style.RESET_ALL,"hello world")

class User:
    
    def test(self,username):
        print(username)

if __name__ == "__main__":
    u=User
    u.test("hah")