# (c) @BGHRFF


class Colors(object):
    st = "\033[1;"  # Bold Style
    RED___ = f"{st}31;40m"
    GREEN_ = f"{st}32;40m"
    YELLOW = f"{st}33;40m"
    BLUE__ = f"{st}34;40m"
    PURPLE = f"{st}35;40m"
    CYAN__ = f"{st}36;40m"
    WHITE_ = f"{st}37;40m"



class Config(object):
    ENTER_IMAGE_PATH = f"\n{Colors.GREEN_}Şəkilin yerləşdiyi yeri qeyd edin: {Colors.CYAN__}"
    CHOOSE_FROM_MENU = "\n" \
                       f"\n{Colors.GREEN_}[{Colors.YELLOW}01{Colors.GREEN_}] Exif məlumatlarını əldə edin" \
                       f"\n{Colors.GREEN_}[{Colors.YELLOW}02{Colors.GREEN_}] Exif məlumatlarını məhv edin" \
                       f"\n{Colors.GREEN_}[{Colors.YELLOW}00{Colors.GREEN_}] Skriptdən çıxın" \
                       "\n" \
                       f"\n{Colors.GREEN_}Seçim edin: {Colors.CYAN__}"
    
    @staticmethod
    def banner():
        BANNER = f"""{Colors.PURPLE}
 ___                              _____      _  __
|_ _|_ __ ___   __ _  __ _  ___  | ____|_  _(_)/ _|
 | || '_ ` _ \ / _` |/ _` |/ _ \ |  _| \ \/ / | |_
 | || | | | | | (_| | (_| |  __/ | |___ >  <| |  _|
|___|_| |_| |_|\__,_|\__, |\___| |_____/_/\_\_|_|
                     |___/{Colors.BLUE__}
                                v1.2  {Colors.CYAN__}
                                BGHRFF@GitHub
"""
        print("\033c")
        print(BANNER)
