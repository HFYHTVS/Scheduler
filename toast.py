from win10toast import ToastNotifier  # 导入系统通知栏

def Toast(name,t1,t2,ico = "icon/timerLogo.ico"):
    toast = ToastNotifier()
        # 有icon的版本
    toast.show_toast(f"成功创建计划 - {name}",
            f"{t1} - {t2}",
            icon_path=ico,
            ) 