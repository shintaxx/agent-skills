#!/usr/bin/env python3
"""
skill-updater.py

master ディレクトリを各ターゲットスキルにコピーし、
SKILL.md 内のプレイスホルダーを適切な設置パスに置換する。
"""

import shutil
from pathlib import Path

# 設定: スキル名と設置場所のマッピング
SKILL_CONFIGS = {
    "cc-skill-creator": ".claude/skills",
    "ag-skill-creator": ".agent/skills",
    "cp-skill-creator": ".github/skills",
}

# プレイスホルダー
PLACEHOLDER_INSTALL_PATH = "{{SKILL_INSTALL_PATH}}"
PLACEHOLDER_SKILL_NAME = "{{SKILL_NAME}}"

# ディレクトリ名
SOURCE_DIR = "master"
TARGET_DIR = "skills"


def main():
    # プロジェクトルート（bin/の親ディレクトリ）を基準にする
    base_path = Path(__file__).parent.parent
    source_path = base_path / SOURCE_DIR
    skills_path = base_path / TARGET_DIR

    # master ディレクトリの存在確認
    if not source_path.exists():
        print(f"エラー: {SOURCE_DIR} ディレクトリが見つかりません")
        return 1

    # skills ディレクトリを作成（存在しない場合）
    skills_path.mkdir(exist_ok=True)

    for skill_name, install_path in SKILL_CONFIGS.items():
        target_path = skills_path / skill_name

        # 既存のディレクトリを削除してからコピー
        if target_path.exists():
            shutil.rmtree(target_path)

        # ディレクトリをコピー
        shutil.copytree(source_path, target_path)
        print(f"コピー完了: {SOURCE_DIR} -> {TARGET_DIR}/{skill_name}")

        # template.md を SKILL.md にリネームしてプレイスホルダーを置換
        template_path = target_path / "template.md"
        skill_md_path = target_path / "SKILL.md"
        if template_path.exists():
            content = template_path.read_text(encoding="utf-8")
            updated_content = content.replace(PLACEHOLDER_INSTALL_PATH, install_path)
            updated_content = updated_content.replace(PLACEHOLDER_SKILL_NAME, skill_name)
            skill_md_path.write_text(updated_content, encoding="utf-8")
            template_path.unlink()  # template.md を削除
            print(f"  -> SKILL.md 作成: プレースホルダーを置換 (name={skill_name}, path={install_path})")
        else:
            print(f"  -> 警告: template.md が見つかりません: {template_path}")

    print("\n全てのスキルの更新が完了しました")
    return 0


if __name__ == "__main__":
    exit(main())
