# Contributing

วิธีการเพิ่มโจทย์เข้าระบบของเว็บ programming.in.th

## Steps

1. Fork repo statements
2. สร้าง branch ใหม่ตามไอดีโจทย์ (สามารถดูวิธีตั้งไอดีได้ในข้อสาม)
3. เพิ่มไฟล์ `.tex` เข้าไป โดยไอดีใช้ดังนี้ `prog_ไอดีโจทย์` เช่น โจทย์ชื่อ A^B Problem จะได้ ID ว่า `prog_a_to_the_b` (ตัวอย่างไฟล์ latex สามารถดูได้ใน repo นี้)

ตัวอย่าง
```tex
\documentclass[11pt,a4paper]{article}

\usepackage{../../templates/style}

\begin{document}

\begin{problem}{ชื่อโจทย์}{standard input}{standard output}{เวลา}{ความจำ}

คำนำโจทย์

\underline{\textbf{โจทย์}} คำอธิบายโจทย์

\InputFile

\textbf{บรรทัดแรก} ข้อมูลนำเข้าบรรทัดแรก

\textbf{บรรทัดที่สอง} ข้อมูลนำเข้าบรรทัดที่สอง

\OutputFile

ข้อมูลส่งออก

\Examples

ใส่ตัวอย่าง Input / Output

\begin{example}
\exmp{5 4
}{9
}%
\end{example}

\Source

ใส่เครดิต

\end{problem}

\end{document}
```
4. Compile latex โดยการรัน script `gen`
5. ส่งอีเมลมาที่ prog.in.th@gmail.com โดยตั้งหัวข้อว่า Manifest & Test Cases for ชื่อโจทย์ (สามารถแนบไฟล์ได้ทาง Firefox Send หรืออื่น ๆ ใน format .zip)
6. เปิด Pull Request มาที่ repo programming-in-th/statements โดยระบุชื่อโจทย์ เช่น Add A^B Problem
