'''
Created on Oct 13, 2018
@author: Tyler McGrew

Copyright <2018> <TYLER MCGREW>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from xml.etree import ElementTree
import os


root = ElementTree.parse('FPGA_Settings.xml')
moduleName = root.find('Module_Name').text.strip()
dir_path = os.path.dirname(os.path.realpath(__file__))
fileName = os.path.join(dir_path,str.format('{}.v', moduleName))


with open('Pin_Assignments.csv','w') as g:
   
	g.write('To,Direction,Location\n\
	AUD_ADCDAT,Input,PIN_D2\n\
	AUD_ADCLRCK,Bidir,PIN_C2\n\
	AUD_BCLK,Bidir,PIN_F2\n\
	AUD_DACDAT,Output,PIN_D1\n\
	AUD_DACLRCK,Bidir,PIN_E3\n\
	AUD_XCK,Output,PIN_E1\n\
	CLOCK2_50,Input,PIN_AG14\n\
	CLOCK3_50,Input,PIN_AG15\n\
	CLOCK_50,Input,PIN_Y2\n\
	EX_IO[6],Bidir,PIN_D9\n\
	EX_IO[5],Bidir,PIN_E10\n\
	EX_IO[4],Bidir,PIN_F14\n\
	EX_IO[3],Bidir,PIN_H14\n\
	EX_IO[2],Bidir,PIN_H13\n\
	EX_IO[1],Bidir,PIN_J14\n\
	EX_IO[0],Bidir,PIN_J10\n\
	HEX0[6],Output,PIN_H22\n\
	HEX0[5],Output,PIN_J22\n\
	HEX0[4],Output,PIN_L25\n\
	HEX0[3],Output,PIN_L26\n\
	HEX0[2],Output,PIN_E17\n\
	HEX0[1],Output,PIN_F22\n\
	HEX0[0],Output,PIN_G18\n\
	HEX1[6],Output,PIN_U24\n\
	HEX1[5],Output,PIN_U23\n\
	HEX1[4],Output,PIN_W25\n\
	HEX1[3],Output,PIN_W22\n\
	HEX1[2],Output,PIN_W21\n\
	HEX1[1],Output,PIN_Y22\n\
	HEX1[0],Output,PIN_M24\n\
	HEX2[6],Output,PIN_W28\n\
	HEX2[5],Output,PIN_W27\n\
	HEX2[4],Output,PIN_Y26\n\
	HEX2[3],Output,PIN_W26\n\
	HEX2[2],Output,PIN_Y25\n\
	HEX2[1],Output,PIN_AA26\n\
	HEX2[0],Output,PIN_AA25\n\
	HEX3[6],Output,PIN_Y19\n\
	HEX3[5],Output,PIN_AF23\n\
	HEX3[4],Output,PIN_AD24\n\
	HEX3[3],Output,PIN_AA21\n\
	HEX3[2],Output,PIN_AB20\n\
	HEX3[1],Output,PIN_U21\n\
	HEX3[0],Output,PIN_V21\n\
	HEX4[6],Output,PIN_AE18\n\
	HEX4[5],Output,PIN_AF19\n\
	HEX4[4],Output,PIN_AE19\n\
	HEX4[3],Output,PIN_AH21\n\
	HEX4[2],Output,PIN_AG21\n\
	HEX4[1],Output,PIN_AA19\n\
	HEX4[0],Output,PIN_AB19\n\
	HEX5[6],Output,PIN_AH18\n\
	HEX5[5],Output,PIN_AF18\n\
	HEX5[4],Output,PIN_AG19\n\
	HEX5[3],Output,PIN_AH19\n\
	HEX5[2],Output,PIN_AB18\n\
	HEX5[1],Output,PIN_AC18\n\
	HEX5[0],Output,PIN_AD18\n\
	HEX6[6],Output,PIN_AC17\n\
	HEX6[5],Output,PIN_AA15\n\
	HEX6[4],Output,PIN_AB15\n\
	HEX6[3],Output,PIN_AB17\n\
	HEX6[2],Output,PIN_AA16\n\
	HEX6[1],Output,PIN_AB16\n\
	HEX6[0],Output,PIN_AA17\n\
	HEX7[6],Output,PIN_AA14\n\
	HEX7[5],Output,PIN_AG18\n\
	HEX7[4],Output,PIN_AF17\n\
	HEX7[3],Output,PIN_AH17\n\
	HEX7[2],Output,PIN_AG17\n\
	HEX7[1],Output,PIN_AE17\n\
	HEX7[0],Output,PIN_AD17\n\
	I2C_SCLK,Output,PIN_B7\n\
	I2C_SDAT,Bidir,PIN_A8\n\
	IRDA_RXD,Input,PIN_Y15\n\
	KEY[3],Input,PIN_R24\n\
	KEY[2],Input,PIN_N21\n\
	KEY[1],Input,PIN_M21\n\
	KEY[0],Input,PIN_M23\n\
	LCD_BLON,Output,PIN_L6\n\
	LCD_DATA[7],Bidir,PIN_M5\n\
	LCD_DATA[6],Bidir,PIN_M3\n\
	LCD_DATA[5],Bidir,PIN_K2\n\
	LCD_DATA[4],Bidir,PIN_K1\n\
	LCD_DATA[3],Bidir,PIN_K7\n\
	LCD_DATA[2],Bidir,PIN_L2\n\
	LCD_DATA[1],Bidir,PIN_L1\n\
	LCD_DATA[0],Bidir,PIN_L3\n\
	LCD_EN,Output,PIN_L4\n\
	LCD_ON,Output,PIN_L5\n\
	LCD_RS,Output,PIN_M2\n\
	LCD_RW,Output,PIN_M1\n\
	LEDG[8],Output,PIN_F17\n\
	LEDG[7],Output,PIN_G21\n\
	LEDG[6],Output,PIN_G22\n\
	LEDG[5],Output,PIN_G20\n\
	LEDG[4],Output,PIN_H21\n\
	LEDG[3],Output,PIN_E24\n\
	LEDG[2],Output,PIN_E25\n\
	LEDG[1],Output,PIN_E22\n\
	LEDG[0],Output,PIN_E21\n\
	LEDR[17],Output,PIN_H15\n\
	LEDR[16],Output,PIN_G16\n\
	LEDR[15],Output,PIN_G15\n\
	LEDR[14],Output,PIN_F15\n\
	LEDR[13],Output,PIN_H17\n\
	LEDR[12],Output,PIN_J16\n\
	LEDR[11],Output,PIN_H16\n\
	LEDR[10],Output,PIN_J15\n\
	LEDR[9],Output,PIN_G17\n\
	LEDR[8],Output,PIN_J17\n\
	LEDR[7],Output,PIN_H19\n\
	LEDR[6],Output,PIN_J19\n\
	LEDR[5],Output,PIN_E18\n\
	LEDR[4],Output,PIN_F18\n\
	LEDR[3],Output,PIN_F21\n\
	LEDR[2],Output,PIN_E19\n\
	LEDR[1],Output,PIN_F19\n\
	LEDR[0],Output,PIN_G19\n\
	SMA_CLKIN,Input,PIN_AH14\n\
	SMA_CLKOUT,Output,PIN_AE23\n\
	SW[17],Input,PIN_Y23\n\
	SW[16],Input,PIN_Y24\n\
	SW[15],Input,PIN_AA22\n\
	SW[14],Input,PIN_AA23\n\
	SW[13],Input,PIN_AA24\n\
	SW[12],Input,PIN_AB23\n\
	SW[11],Input,PIN_AB24\n\
	SW[10],Input,PIN_AC24\n\
	SW[9],Input,PIN_AB25\n\
	SW[8],Input,PIN_AC25\n\
	SW[7],Input,PIN_AB26\n\
	SW[6],Input,PIN_AD26\n\
	SW[5],Input,PIN_AC26\n\
	SW[4],Input,PIN_AB27\n\
	SW[3],Input,PIN_AD27\n\
	SW[2],Input,PIN_AC27\n\
	SW[1],Input,PIN_AC28\n\
	SW[0],Input,PIN_AB28\n\
	UART_CTS,Output,PIN_G14\n\
	UART_RTS,Input,PIN_J13\n\
	UART_RXD,Input,PIN_G12\n\
	UART_TXD,Output,PIN_G9\n\
	VGA_B[7],Output,PIN_D12\n\
	VGA_B[6],Output,PIN_D11\n\
	VGA_B[5],Output,PIN_C12\n\
	VGA_B[4],Output,PIN_A11\n\
	VGA_B[3],Output,PIN_B11\n\
	VGA_B[2],Output,PIN_C11\n\
	VGA_B[1],Output,PIN_A10\n\
	VGA_B[0],Output,PIN_B10\n\
	VGA_BLANK_N,Output,PIN_F11\n\
	VGA_CLK,Output,PIN_A12\n\
	VGA_G[7],Output,PIN_C9\n\
	VGA_G[6],Output,PIN_F10\n\
	VGA_G[5],Output,PIN_B8\n\
	VGA_G[4],Output,PIN_C8\n\
	VGA_G[3],Output,PIN_H12\n\
	VGA_G[2],Output,PIN_F8\n\
	VGA_G[1],Output,PIN_G11\n\
	VGA_G[0],Output,PIN_G8\n\
	VGA_HS,Output,PIN_G13\n\
	VGA_R[7],Output,PIN_H10\n\
	VGA_R[6],Output,PIN_H8\n\
	VGA_R[5],Output,PIN_J12\n\
	VGA_R[4],Output,PIN_G10\n\
	VGA_R[3],Output,PIN_F12\n\
	VGA_R[2],Output,PIN_D10\n\
	VGA_R[1],Output,PIN_E11\n\
	VGA_R[0],Output,PIN_E12\n\
	VGA_SYNC_N,Output,PIN_C10\n\
	VGA_VS,Output,PIN_C13')
	
	
with open(fileName, 'w') as f:

	f.write(str.format('module {} (\n', moduleName))
	  
	if root.find('Components/Clock/Enabled').text.strip().lower() == 'true':
		f.write('\t//---------------------------------- Clock\n')
		f.write('\tCLOCK_50,\n')
		f.write('\tCLOCK2_50,\n')
		f.write('\tCLOCK3_50,\n\n')
	  
	if root.find('Components/LED_Red/Enabled').text.strip().lower() == 'true':
		f.write('\t//---------------------------------- LED_Red\n')
		f.write('\tLED_R,\n\n')
		  
	if root.find('Components/LED_Green/Enabled').text.strip().lower() == 'true':
		f.write('\t//---------------------------------- LED_Green\n')
		f.write('\tLED_G,\n\n')
		  
	if root.find('Components/Button/Enabled').text.strip().lower() == 'true':
		f.write('\t//---------------------------------- Button\n')
		f.write('\tBUTTON,\n\n')
		  
	if root.find('Components/VGA/Enabled').text.strip().lower() == 'true':
		f.write('\t//---------------------------------- VGA\n')
		f.write('\tVGA_R,\n')
		f.write('\tVGA_G,\n')
		f.write('\tVGA_B,\n')
		f.write('\tVGA_CLK,\n')
		f.write('\tVGA_SYNC_N,\n')
		f.write('\tVGA_BLANK_N,\n')
		f.write('\tVGA_HS_N,\n')
		f.write('\tVGA_VS_N,\n\n')
	  
	if root.find('Components/Audio/Enabled').text.strip().lower() == 'true':
		f.write('\t//---------------------------------- Audio\n')
		f.write('\tAUD_ADCDAT,\n')
		f.write('\tAUD_ADCLRCK,\n')
		f.write('\tAUD_BCLK,\n')
		f.write('\tAUD_DACDAT,\n')
		f.write('\tAUD_DACLRCK,\n')
		f.write('\tAUD_XCK,\n')
		f.write('\tI2C_SCLK,\n')
		f.write('\tI2C_SDAT,\n\n')
		  
	if root.find('Components/IR_Receiver/Enabled').text.strip().lower() == 'true':
		f.write('\t//---------------------------------- IR_Receiver\n')
		f.write('\tIRDA_RXD,\n\n')
		  
	if root.find('Components/RS_232/Enabled').text.strip().lower() == 'true':
		f.write('\t//---------------------------------- RS_232\n')
		f.write('\tUART_CTS,\n')
		f.write('\tUART_RTS,\n')
		f.write('\tUART_RXD,\n')
		f.write('\tUART_TXD,\n\n')
	  
	if root.find('Components/Seven_Segment/Enabled').text.strip().lower() == 'true':
		f.write('\t//---------------------------------- Seven_Segment\n')
		f.write('\tHEX0,\n')
		f.write('\tHEX1,\n')
		f.write('\tHEX2,\n')
		f.write('\tHEX3,\n')
		f.write('\tHEX4,\n')
		f.write('\tHEX5,\n')
		f.write('\tHEX6,\n')
		f.write('\tHEX7,\n\n')
		  
	if root.find('Components/Switch/Enabled').text.strip().lower() == 'true':
		f.write('\t//---------------------------------- Switch\n')
		f.write('\tSW,\n\n')
		  
	if root.find('Components/LCD/Enabled').text.strip().lower() == 'true':
		f.write('\t//---------------------------------- LCD\n')
		f.write('\tLCD_DATA,\n')
		f.write('\tLCD_BLON,\n')
		f.write('\tLCD_EN,\n')
		f.write('\tLCD_ON,\n')
		f.write('\tLCD_RS,\n')
		f.write('\tLCD_RW,\n\n')
	  
	if root.find('Components/SMA/Enabled').text.strip().lower() == 'true':
		f.write('\t//---------------------------------- SMA\n')
		f.write('\tSMA_CLKIN,\n')
		f.write('\tSMA_CLKOUT,\n\n')
		
	if root.find('Components/EX_IO/Enabled').text.strip().lower() == 'true':
		f.write('\t//---------------------------------- EX_IO\n')
		f.write('\tEX_IO,\n\n')
	
with open(fileName, 'r') as f:
	
	lines = f.readlines()
	lines[-2] = lines[-2].replace(',','')
	lines[-1] = lines[-1].replace('\n','')
	
	
with open(fileName, 'w') as f:

	f.write(''.join(lines))
	f.write(');\n\n\n')
	f.write('//------------------------------------------------------------------\n')
	f.write('//                 -- Input/Output Declarations --                  \n')
	f.write('//------------------------------------------------------------------\n\n')
	  
	if root.find('Components/Clock/Enabled').text.strip().lower() == 'true':
		f.write('//---------------------------------- Clock\n')
		f.write('input CLOCK_50, CLOCK2_50, CLOCK3_50;\n\n')
	  
	if root.find('Components/LED_Red/Enabled').text.strip().lower() == 'true':
		f.write('//---------------------------------- LED_Red\n')
		f.write('output [17:0]LED_R;\n\n')
		  
	if root.find('Components/LED_Green/Enabled').text.strip().lower() == 'true':
		f.write('//---------------------------------- LED_Green\n')
		f.write('output [8:0]LED_G;\n\n')
		  
	if root.find('Components/Button/Enabled').text.strip().lower() == 'true':
		f.write('//---------------------------------- Button\n')
		f.write('input [3:0]BUTTON;\n\n')
		  
	if root.find('Components/VGA/Enabled').text.strip().lower() == 'true':
		f.write('//---------------------------------- VGA\n')
		f.write('output [7:0]VGA_R;\n')
		f.write('output [7:0]VGA_G;\n')
		f.write('output [7:0]VGA_B;\n')
		f.write('output VGA_CLK, VGA_SYNC_N, VGA_BLANK_N, VGA_HS, VGA_VS;\n\n')
	  
	if root.find('Components/Audio/Enabled').text.strip().lower() == 'true':
		f.write('//---------------------------------- Audio\n')
		f.write('input AUD_ADCDAT;\n')
		f.write('inout AUD_ADCLRCK;\n')
		f.write('inout AUD_BCLK;\n')
		f.write('output AUD_DACDAT;\n')
		f.write('inout AUD_DACLRCK;\n')
		f.write('output AUD_XCK;\n')
		f.write('output I2C_SCLK;\n')
		f.write('inout I2C_SDAT;\n\n')
		  
	if root.find('Components/IR_Receiver/Enabled').text.strip().lower() == 'true':
		f.write('//---------------------------------- IR_Receiver\n')
		f.write('input IRDA_RXD;\n\n')
		  
	if root.find('Components/RS_232/Enabled').text.strip().lower() == 'true':
		f.write('//---------------------------------- RS_232\n')
		f.write('input UART_RTS, UART_RXD;\n')
		f.write('output UART_CTS, UART_TXD;\n\n')
	  
	if root.find('Components/Seven_Segment/Enabled').text.strip().lower() == 'true':
		f.write('//---------------------------------- Seven_Segment\n')
		f.write('output [6:0]HEX0;\n')
		f.write('output [6:0]HEX1;\n')
		f.write('output [6:0]HEX2;\n')
		f.write('output [6:0]HEX3;\n')
		f.write('output [6:0]HEX4;\n')
		f.write('output [6:0]HEX5;\n')
		f.write('output [6:0]HEX6;\n')
		f.write('output [6:0]HEX7;\n\n')
		  
	if root.find('Components/Switch/Enabled').text.strip().lower() == 'true':
		f.write('//---------------------------------- Switch\n')
		f.write('input [17:0]SW;\n\n')
		  
	if root.find('Components/LCD/Enabled').text.strip().lower() == 'true':
		f.write('//---------------------------------- LCD\n')
		f.write('inout [7:0]LCD_DATA;\n')
		f.write('output LCD_BLON, LCD_EN, LCD_ ON, LCD_RS, LCD_RW;\n\n')
	  
	if root.find('Components/SMA/Enabled').text.strip().lower() == 'true':
		f.write('//---------------------------------- SMA\n')
		f.write('input SMA_CLKIN;\n')
		f.write('output SMA_CLKOUT;\n\n')
		  
	if root.find('Components/EX_IO/Enabled').text.strip().lower() == 'true':
		f.write('//---------------------------------- EX_IO\n')
		f.write('inout [6:0]EX_IO;\n\n')
	
	f.write('//------------------------------------------------------------------\n')
	f.write('//                 -- Begin Declarations & Coding --                  \n')
	f.write('//------------------------------------------------------------------\n\n')
	
	f.write('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
	f.write('endmodule')