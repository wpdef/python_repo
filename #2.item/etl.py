import os
import re
import pandas as pd
import sqlite3


def load_column_mapping(properties_path):
    """加载column_mapping.propties文件为字典"""
    column_mapping = {}
    with open(properties_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and '=' in line:
                csv_col, db_col = line.split('=', 1)
                column_mapping[csv_col.strip()] = db_col.strip()
    return column_mapping


def process_csv_files(config_dir):
    # 加载列映射配置
    properties_path = ".\\column_mapping.propties"

    if not os.path.exists(properties_path):
        print(f"配置文件 {properties_path} 不存在")
        return
    column_mapping = load_column_mapping(properties_path)
    required_columns = list(column_mapping.keys())

    # 数据库连接参数（数据库文件存放在配置目录下）
    db_path = ".\\items.db"

    # 创建数据库表
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS items (
        item_code TEXT,
        item_title TEXT,
        category TEXT,
        brand TEXT,
        mpn TEXT,
        outer_id TEXT,
        shelf_on_at TEXT,
        shelf_off_at TEXT,
        created_at TEXT,
        updated_at TEXT,
        state TEXT,
        store_code TEXT
    )
    """
    with sqlite3.connect(db_path) as conn:
        conn.execute(create_table_sql)
        conn.commit()

    # 遍历目录下的CSV文件
    for filename in os.listdir(".\\"):
        if not filename.endswith('.csv') or filename == 'column_mapping.propties':
            continue

        file_path = os.path.join(".\\", filename)
        base_name, ext = os.path.splitext(filename)
        new_name = None

        try:
            # 校验store_code格式
            if not re.fullmatch(r'^JD_\d+$', base_name):
                raise ValueError(f"无效的store_code格式: {base_name}")
            store_code = base_name

            # 读取CSV文件
            df = pd.read_csv(file_path)

            # 校验CSV列
            csv_columns = set(df.columns)
            missing = [col for col in required_columns if col not in csv_columns]
            if missing:
                raise ValueError(f"缺少必要的列: {', '.join(missing)}")

            # 添加store_code列并重命名列
            df['store_code'] = store_code
            df.rename(columns=column_mapping, inplace=True)
            target_columns = list(column_mapping.values()) + ['store_code']
            df = df[target_columns]

            # 写入数据库
            with sqlite3.connect(db_path) as conn:
                df.to_sql('items', conn, if_exists='append', index=False)

            # 标记处理成功
            new_name = f"{filename}.COMPLETED"

        except Exception as e:
            print(f"处理文件 {filename} 失败: {e}")
            new_name = f"{filename}.FAILED"

        # 重命名文件
        if new_name:
            try:
                os.rename(file_path, os.path.join(".\\", new_name))
            except Exception as e:
                print(f"重命名文件 {filename} 失败: {e}")


if __name__ == "__main__":
    # 配置目录路径，根据实际情况修改
    config_dir = '\item'
    process_csv_files(config_dir)