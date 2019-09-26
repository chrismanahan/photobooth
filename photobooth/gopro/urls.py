HOST = "http://10.5.5.9/gp/gpControl"
COMMAND = HOST + "/command"
SETTING = HOST + "/setting"

TRIGGER_SHUTTER = COMMAND + "/shutter?p=1"
STOP_VIDEO = COMMAND + "/shutter?p=0"

DEFAULT_BOOT_VIDEO = SETTING + "/setting/53/0"
DEFAULT_BOOT_PHOTO = SETTING + "/setting/53/1"
DEFAULT_BOOT_MULTISHOT = SETTING + "/setting/53/2"

LOCATE_ON = COMMAND + "/system/locate?p=1"
LOCATE_OFF = COMMAND + "/system/locate?p=0"