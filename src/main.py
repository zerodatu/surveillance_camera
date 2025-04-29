#!/usr/bin/env python3
import cv2
import sys

def show_webcam_feed():
    """Webカメラに接続し、リアルタイムで映像を表示する"""

    # デフォルトのWebカメラ（通常はインデックス0）に接続
    cap = cv2.VideoCapture(0)

    # カメラが正常に開けたか確認
    if not cap.isOpened():
        print("エラー: Webカメラを開けませんでした。")
        sys.exit()

    print("Webカメラの映像を表示します。'q'キーを押すと終了します。")

    while True:
        # フレームを1枚読み込む
        ret, frame = cap.read()

        # フレームの読み込みに失敗した場合（カメラが切断されたなど）
        if not ret:
            print("エラー: フレームを読み込めませんでした。")
            break

        # フレームをウィンドウに表示
        cv2.imshow('Webcam Feed', frame)

        # 'q'キーが押されたらループを抜ける (1ミリ秒待機)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # キャプチャを解放
    cap.release()
    # すべてのOpenCVウィンドウを閉じる
    cv2.destroyAllWindows()
    print("プログラムを終了しました。")

def main():
    """メイン処理"""
    print("Hello, Python!")


if __name__ == "__main__":
    main()
