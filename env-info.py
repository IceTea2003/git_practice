import sys
import site

sys.stdout.reconfigure(encoding="utf-8")

def get_env_info():
    info = {
        "executable": sys.executable,
        "version": sys.version,
        "prefix": sys.prefix,
        "site_packages": site.getsitepackages(),
    }
    return info

if __name__ == "__main__":
    info = get_env_info()
    print("=" * 60)
    print("*当前 Python 环境信息*")
    print("=" * 60)
    print(f"解释器路径: {info['executable']}")
    print(f"Python 版本: {info['version'].split()[0]}")
    print(f"环境前缀: {info['prefix']}")
    print(f"site-packages: {info['site_packages'][0]}")
    print("=" * 60)
    
    if ".venv" in info['executable']:
        print("✅ 当前环境: 项目虚拟环境 (.venv)")
    elif "venv" in info['executable'] or "env" in info['executable']:
        print("✅ 当前环境: 自定义虚拟环境")
    else:
        print("⚠️  当前环境: 系统 Python (请谨慎操作)")
        print("   原因: 直接使用系统 Python 时，pip install 会将包安装到全局 site-packages，")
        print("         可能污染系统环境、与其他项目依赖冲突，甚至影响系统自带工具。")
        print("   建议: 使用虚拟环境隔离依赖，例如:")
        print("         uv venv            # 创建 .venv 虚拟环境")
        print("         python -m venv .venv   # 或用标准库创建")