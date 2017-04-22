
import platform

if platform.system() == 'Windows':
    from ctypes import windll, byref, Structure, c_short, c_ushort



    SHORT = c_short
    WORD = c_ushort

    class COORD(Structure):
        """struct in wincon.h."""
        _fields_ = [
            ("X", SHORT),
            ("Y", SHORT)]

    class SMALL_RECT(Structure):
        """struct in wincon.h."""
        _fields_ = [
            ("Left", SHORT),
            ("Top", SHORT),
            ("Right", SHORT),
            ("Bottom", SHORT)]


    class CONSOLE_SCREEN_BUFFER_INFO(Structure):
        """struct in wincon.h."""
        _fields_ = [
            ("dwSize", COORD),
            ("dwCursorPosition", COORD),
            ("wAttributes", WORD),
            ("srWindow", SMALL_RECT),
            ("dwMaximumWindowSize", COORD)]

    STD_OUTPUT_HANDLE = -11

    black     = 0x0000
    blue      = 0x0001
    green     = 0x0002
    cyan      = 0x0003
    red       = 0x0004
    magenta   = 0x0005
    yellow    = 0x0006
    grey      = 0x0007

    BACKGROUND_BLACK     = 0x0000
    BACKGROUND_BLUE      = 0x0010
    BACKGROUND_GREEN     = 0x0020
    BACKGROUND_CYAN      = 0x0030
    BACKGROUND_RED       = 0x0040
    BACKGROUND_MAGENTA   = 0x0050
    BACKGROUND_YELLOW    = 0x0060
    BACKGROUND_GREY      = 0x0070

    stdout_handle = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    SetConsoleTextAttribute = windll.kernel32.SetConsoleTextAttribute
    GetConsoleScreenBufferInfo = windll.kernel32.GetConsoleScreenBufferInfo

    def set_color(color):
        SetConsoleTextAttribute(stdout_handle, color)

    
    def get_color():
        csbi = CONSOLE_SCREEN_BUFFER_INFO()
        GetConsoleScreenBufferInfo(stdout_handle, byref(csbi))
        return csbi.wAttributes



    if __name__ == "__main__":
        reset = get_color()
        print("Test")
        set_color(red)
        print("stuff")
        set_color(reset)
        print("Test")

        set_color(BACKGROUND_BLUE)
        print(" ")
        print(" "*20)
        print(" ")
        set_color(reset)
        print("Test")

