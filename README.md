# ロジックIC時計  
ロジックICとUV-EPROMで時計を作ったのでその資料を．  
ROMに書き込む7segインクリメンタテーブルがメインです．(7seg_table.bin)  
テーブルのアドレスマップはこのようになっています．
![アドレスマップ](https://github.com/cherry-takuan/logic_clock/blob/main/address_map.png)

circuit以下に回路図を載せています．良ければぜひ．

解説等は以下のページを参照のこと．
[ロジックIC時計](https://cherry-takuan.org/article/?id=42)

このページを参考に使えそうならばぜひ使ってください．生成したコードについては特に説明はしませんが，patter.py内で7segのパターンおよび状態の遷移を記述しています．変更する場合はここら辺をいじるとできるはずです．