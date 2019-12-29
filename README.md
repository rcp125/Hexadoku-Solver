# Hexadoku-Solver
Hexadoku is a 16x16 variant to the traditional Sudoku board. The rows & columns range from 0 to F. This Flask application allows users to upload an unsolved Hexadoku board and returns a solved version.

### How to Upload
1) Text File
  a) Format: characters should be separated by a "tab" and blank spots should be marked by "-"
2) Image (currently unsupported)
  a) Format: Make sure all letters are visible on the board.
 
 ### Features to Come
 1) Resolve last column bug. Script solves Hexadoku board correctly but does not update solved values for elements in the last column
 2) Implement OCR to read characters from image and export to text file Hexadoku board
 3) Allow users to download text file with solved board
