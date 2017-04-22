
import platform

if platform.system() == 'Windows':
    from ctypes import windll

    STD_OUTPUT_HANDLE = -11

    reset     = 0x0000
    blue      = 0x0001
    green     = 0x0002
    cyan      = 0x0003
    red       = 0x0004
    magenta   = 0x0005
    yellow    = 0x0006
    grey      = 0x0007

    stdout_handle = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    SetConsoleTextAttribute = windll.kernel32.SetConsoleTextAttribute

    def set_text_color(color):
        SetConsoleTextAttribute(stdout_handle, color)



    if __name__ == "__main__":
        set_text_color(red)
        print("stuff")
        set_text_color(reset)

