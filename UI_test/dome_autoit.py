import autoit

class MouseControl(object):
    '''
    AutoIt鼠标相关操作
    '''
    def __init__(self):
        '''
        Constructor
        '''
        
    def click(self, title, text, x, y, button="main", clicks=1):
        '''
        :description 执行鼠标点击操作
        '''
        pos = autoit.win_get_pos(title, text=text)
        autoit.mouse_click(button, x + pos[0], y + pos[1], clicks=clicks)
        
    def move(self, title, text, x, y):
        '''
        :description 移动鼠标指针
        '''
        pos = autoit.win_get_pos(title, text=text)
        autoit.mouse_move(x + pos[0], y + pos[1])
        
    def drag(self, title, text, x1, y1, x2, y2):
        '''
        :description 执行鼠标拖拽操作
        '''
        pos = autoit.win_get_pos(title, text=text)
        autoit.mouse_click_drag(x1 + pos[0], y1 + pos[1], x2 + pos[0], y2 + pos[1])
        
    def wheel(self, direction="up"):
        '''
        :description 产生向上或向下滚动鼠标滚轮事件.仅支持NT/2000/XP及更高.
        '''
        autoit.mouse_wheel(direction)

import autoit

class ProcessControl(object):
    '''
    AutoIt进程相关操作
    '''
    
    def __init__(self, processName):
        '''
        Constructor
        '''
        self.processName = processName
        
    def close(self):
        '''
        :description 终止某个进程
        :return 1:成功; 0:失败.
        '''
        return autoit.process_close(self.processName)
        
    def exists(self):
        '''
        :description 检查指定进程是否存在
        :return PID:成功; 0:进程不存在.
        '''
        return autoit.process_exists(self.processName)

class WinControl(object):
    '''
    AutoIt窗口相关操作
    '''

    def __init__(self, title, text=''):
        '''
        Constructor
        '''
        self.title = title
        self.text = text
        
    def activate(self):
        '''
        :description 激活指定的窗口(设置焦点到该窗口,使其成为活动窗口).
        :return PID:窗口存在; 0:窗口不存在.
        '''        
        return autoit.win_activate(self.title, text=self.text)
        
    def close(self):
        '''
        :description 关闭指定窗口.
        :return 1:成功; 0:窗口不存在.
        '''        
        return autoit.win_close(self.title, text=self.text)
        
    def exists(self):
        '''
        :description 检查指定的窗口是否存在.
        :return 1:窗口存在; 0:窗口不存在.
        '''
        return autoit.win_exists(self.title, text=self.text)
        
    def getPos(self):
        '''
        :description 获取指定窗口的坐标位置和大小等属性.
        :return Returns left, top, right, bottom    (x1,y1,x2,y2)
        '''
        return autoit.win_get_pos(self.title, text=self.text)
    
    def getProcess(self):
        '''
        :description 获取指定窗口关联的进程ID(PID).
        :return PID:成功, -1:失败.
        '''
        return autoit.win_get_process(self.title, text=self.text)  
    
    def getText(self, buf_size=256):
        '''
        :description 获取指定窗口中的文本.
        :return  指定窗口里包含的文本:成功; 0:失败(没有匹配的窗口).
        '''        
        return autoit.win_get_text(self.title, buf_size, text=self.text)
          
    def kill(self):
        '''
        :description 强行关闭指定窗口.
        :return  1:无论成功失败.
        '''        
        return autoit.win_kill(self.title, text=self.text)
        
    def move(self, x, y, width, height):
        '''
        :description 移动指定的窗口或调整窗口的大小.
        :return PID:成功, 0:失败(窗口不存在).
        '''
        return autoit.win_move(self.title, x, y, width, height, text=self.text)         
    
    def setState(self, flag):
        '''
        :description 显示,隐藏,最小化,最大化或还原一个窗口.
        :param flag: The "show" flag of the executed program:
                    1 = 显示
                    2 = 最小化/隐藏
                    3 = 最大化
                    4 = 还原
        :return 1:成功, 0:失败(窗口不存在).
        '''
        return autoit.win_set_state(self.title, flag, text=self.text)
        
    def wait(self, timeout=5):
        '''
        :description 暂停脚本的执行直至指定窗口存在(出现)为止.
        timeout 单位为秒.
        :return PID:成功, 0:失败(超时).
        '''
        return autoit.win_wait(self.title, timeout, text=self.text)            
        
    def waitActive(self, timeout=5):
        '''
        :description 暂停脚本的执行直至指定窗口被激活(成为活动状态)为止.
        timeout 单位为秒.
        :return PID:成功, 0:失败(超时).
        '''
        return autoit.win_wait_active(self.title, timeout, text=self.text)         
        
    def waitClose(self, timeout=5):
        '''
        :description 暂停脚本的执行直至所指定窗口不再存在为止.
        timeout 单位为秒.
        :return 1:成功, 0:失败(超时).
        '''
        return autoit.win_wait_close(self.title, timeout, text=self.text)        
        
    def waitNotActive(self, timeout=5):
        '''
        :description 暂停脚本的执行直至指定窗口不是激活状态为止.
        timeout 单位为秒.
        :return 1:成功, 0:失败(超时).
        '''
        return autoit.win_wait_not_active(self.title, timeout, text=self.text)              
        
    def controlClick(self, control, button="main", clicks=1):
        '''
        :description 向指定控件发送鼠标点击命令.
        '''
        autoit.control_click(self.title, control, text=self.text, button=button, clicks=clicks)
        
    def controlCommand(self, control, command, extra="", buf_size=256):
        '''
        :description 向指定控件发送命令.
        :param command, extra:                         :return
                    "IsVisible", ""                    1:可见; 0:不可见
                    "IsEnabled", ""                    1:可用; 0:禁用
                    "ShowDropDown", ""                弹出/下拉 组合框(ComboBox)的列表.
                    "HideDropDown", ""                收回/隐藏 组合框(ComboBox)的列表.
                    "AddString", "string"                在 ListBox 或 ComboBox 的编辑框后面附加指定字符串.
                    "DelString", 出现次序                                删除在 ListBox 或 ComboBox 的编辑框中指定的字符串(从0开始).
                    "FindString", "string"                返回在 ListBox 或 ComboBox 的编辑框中与指定字符串匹配项目的出现次序(从0开始).
                    "SetCurrentSelection", 出现次序            通过指定出现次序(从0开始)把 ListBox 或 ComboBox 的当前选择项设为指定的项目.
                    "SelectString","string"            通过指定字符串把 ListBox 或 ComboBox 的当前选择项设为匹配字符串的项目.
                    "IsChecked", ""                    若目标按钮(复选框/单选框)被选中则返回值为1,否则为0.
                    "Check", ""                        使目标按钮(复选框/单选框)变为选中状态.
                    "UnCheck", ""                        使目标按钮(复选框/单选框)变为非选中状态.
                    "GetCurrentLine", ""                    返回在目标编辑框中插入符(caret,光标)的所在行号.
                    "GetCurrentCol", ""                    返回在目标编辑框中插入符(caret,光标)的所在列号.
                    "GetCurrentSelection", ""                返回 ListBox 或 ComboBox 控件当前选中的项目名.
                    "GetLineCount", ""                        返回目标编辑框中的总行数.
                    "GetLine", 行号                                        返回目标编辑框中指定行的文本内容.
                    "GetSelected", ""                    返回目标编辑框中的(用户用鼠标或其它方式)选定的文本.
                    "EditPaste", 'string'                在目标编辑框中插入符(caret)所在位置后插入指定字符串.
                    "CurrentTab", ""                    返回在 SysTabControl32 控件中当前显示的标签编号(从1开始).
                    "TabRight", ""                        使 SysTabControl32 控件切换到(右边的)下一个标签.
                    "TabLeft", ""                        使 SysTabControl32 控件切换到(左边的)下一个标签. 
                    "SendCommandID", 命令 ID            模拟 WM_COMMAND 消息. 通常用于 ToolbarWindow32 控件 - 使用Au3Info的工具栏标签得到命令ID.
        '''        
        return autoit.control_command(self.title, control, command, buf_size, text=self.text, extra=extra)
        
    def controlListView(self, control, command, extra1, extra2="", buf_size=256):
        '''
        :description 向指定的 ListView32 控件发送命令.
        :param command, extra1, extra2:                         :return
                    "DeSelect", 从[, 到]                        取消选定从"从"开始直到"到"的一个或多个项目. 
                    "FindItem", "搜索字符串" [, 子项目]            返回与给定字符串匹配的项目的位置.若未找到指定字符串则返回值为 -1. 
                    "GetItemCount"                                返回列表中项目的数量. 
                    "GetSelected" [, 选项]                        返回当前选中项目的位置.若 选项=0(默认)则只返回选中的第一个项目;若 选项=1 则返回由竖线"|"作为分隔符的所有选中项目,例如:"0|3|4|10".若没有选中任何项目则返回一个空字符串"". 
                    "GetSelectedCount"                            返回选中项目的数量. 
                    "GetSubItemCount"                            返回子项目的数量. 
                    "GetText", 项目, 子项目                                            返回指定项目/子项目的文本. 
                    "IsSelected", 项目                                                    若指定项目被选中则返回值为1,否则返回值为0. 
                    "Select", 从[, 到]                            选中一个或多个项目(请参考第一个命令). 
                    "SelectAll"                                    选中所有项目. 
                    "SelectClear"                                取消所有项目的选中状态. 
                    "SelectInvert"                                切换当前的选中状态. 
                    "ViewChange", "视图"                        切换当前的视图.可用的视图包括"list"(列表),"details"(详细信息),"smallicons"(小图标),"largeicons"(大图标). 
        '''        
        return autoit.control_list_view(self.title, control, command, buf_size, text=self.text, extra1=extra1, extra2=extra2)        
    
    def controlDisable(self, control):
        '''
        :description 禁用或使某控件变成灰色不可用状态.
        :return 1:成功; 0:失败.
        '''        
        return autoit.control_disable(self.title, control, text=self.text)
        
    def controlEnable(self, control):
        '''
        :description 使灰色按钮/控件变为"可用"状态.
        :return 1:成功; 0:失败.
        '''        
        return autoit.control_enable(self.title, control, text=self.text)        
        
    def controlFocus(self, control):
        '''
        :description 设置输入焦点到指定窗口的某个控件上.
        :return 1:成功; 0:失败.
        '''        
        return autoit.control_focus(self.title, control, text=self.text)  
        
    def controlGetText(self, control):
        '''
        :description 获取指定控件上的文本.
        :return 文本内容:成功; 空:失败.
        '''        
        return autoit.control_get_text(self.title, control, text=self.text)   
        
    def controlSend(self, control, send_text, mode=0 ):    
        '''
        :description 向指定的控件发送字符串.
        :param mode: 0:按特殊字符含义发送(默认); 1:原样发送.
        :return 1:成功; 0:失败(窗口/控件未找到).
        '''        
        return autoit.control_send(self.title, control, send_text, mode, text=self.text)   
        
    def controlSetText(self, control, control_text):
        '''
        :description 修改指定控件的文本.
        :return 1:成功; 0:失败(窗口/控件未找到).
        '''        
        return autoit.control_set_text(self.title, control, control_text, text=self.text)   
           
    def controlTreeView(self, control, command, extra, buf_size=256):
        '''
        :description 发送一个命令到 TreeView32 控件.(子节点不好用*)
        :param command, extra                             :return
        "Check", "项目"                                             选中一个项目 (如果项目支持选中,这里指项目带有选择框). 
        "Collapse", "项目"                                          折叠一个项目节点,使它隐藏它的子项目. 
        "Exists", "项目"         *都返回1*                      如果项目存在返回 1,否则返回 0. 
        "Expand", "项目"                                           展开一个项目节点,使它显示它的子项目. 
        "GetItemCount", "项目"                                 返回所选项目的子项目数量. 
        "GetSelected" [, 使用索引]                             返回当前所选项目的文本参考信息(如果使用索引设置为1将会返回所选项目索引位置). 
        "GetText", "项目"                                          返回项目文本. 
        "IsChecked"                                                  返回项目选中状态. 1:被选中, 0:未被选中, -1:没要选择框. 
        "Select", "项目"                                             选择一个项目. 
        "Uncheck", "项目"                                         取消项目选中状态 (如果项目支持选中,这里指项目带有选择框). 
        '''        
        return autoit.control_tree_view(self.title, control, command, text=self.text, buf_size=buf_size, extra=extra)          
        
    def statusbarGetText(self, part=1, buf_size=256):
        '''
        :description 获取标准状态栏控件的文本.
        :return 文本内容:成功; 空字符串:失败(无法读取文本).
        '''        
        return autoit.statusbar_get_text(self.title, self.text, part, buf_size)  
    
# win = WinControl(title='打开')
# win.controlClick()
# win.controlSetText()