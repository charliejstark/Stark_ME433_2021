#include<xc.h>           // processor SFR definitions
#include<sys/attribs.h>  // __ISR macro
#include<stdio.h>

#include "i2c_master_noint.h"
#include "spi.h"
#include "ST7789.h"
#include "font.h"

#include "LSM6DS33.h"


// DEVCFG0
#pragma config DEBUG = OFF // disable debugging
#pragma config JTAGEN = OFF // disable jtag
#pragma config ICESEL = ICS_PGx1 // use PGED1 and PGEC1
#pragma config PWP = OFF // disable flash write protect
#pragma config BWP = OFF // disable boot write protect
#pragma config CP = OFF // disable code protect

// DEVCFG1
#pragma config FNOSC = FRCPLL // use internal oscillator with pll
#pragma config FSOSCEN = OFF // disable secondary oscillator
#pragma config IESO = OFF // disable switching clocks
#pragma config POSCMOD = OFF // internal RC
#pragma config OSCIOFNC = OFF // disable clock output
#pragma config FPBDIV = DIV_1 // divide sysclk freq by 1 for peripheral bus clock
#pragma config FCKSM = CSDCMD // disable clock switch and FSCM
#pragma config WDTPS = PS1048576 // use largest wdt
#pragma config WINDIS = OFF // use non-window mode wdt
#pragma config FWDTEN = OFF // wdt disabled
#pragma config FWDTWINSZ = WINSZ_25 // wdt window at 25%

// DEVCFG2 - get the sysclk clock to 48MHz from the 8MHz crystal
#pragma config FPLLIDIV = DIV_2 // divide input clock to be in range 4-5MHz
#pragma config FPLLMUL = MUL_24 // multiply clock after FPLLIDIV
#pragma config FPLLODIV = DIV_2 // divide clock after FPLLMUL to get 48MHz

// DEVCFG3
#pragma config USERID = 0 // some 16bit userid, doesn't matter what
#pragma config PMDL1WAY = OFF // allow multiple reconfigurations
#pragma config IOL1WAY = OFF // allow multiple reconfigurations



int main() {

    __builtin_disable_interrupts(); // disable interrupts while initializing things

    // set the CP0 CONFIG register to indicate that kseg0 is cacheable (0x3)
    __builtin_mtc0(_CP0_CONFIG, _CP0_CONFIG_SELECT, 0xa4210583);

    // 0 data RAM access wait states
    BMXCONbits.BMXWSDRM = 0x0;

    // enable multi vector interrupts
    INTCONbits.MVEC = 0x1;

    // disable JTAG to get pins back
    DDPCONbits.JTAGEN = 0;
    
    // do your TRIS and LAT commands here
    // Pin 12 is A4, pin 11 is B4
    TRISBbits.TRISB4 = 1;
    TRISAbits.TRISA4 = 0;
    LATAbits.LATA4   = 0;
    
    // HW11
    initSPI();
    i2c_master_setup();
    LCD_init();
    
    __builtin_enable_interrupts(); // enable interrupts after initializing things

    char m[50];
    short FPS = 0;
    
    unsigned char data[14];
    
    short newData[7];
    int kk;
    
    LCD_clearScreen(BLACK);
    
    
    
    i2c_write(LSM6DS33_ADDRESS, CTRL1_XL, my_CTRL1_XL);
    i2c_write(LSM6DS33_ADDRESS, CTRL2_G,  my_CTRL2_G);
    i2c_write(LSM6DS33_ADDRESS, CTRL3_C,  my_CTRL3_C);
    
    
    sprintf(m, "Charles Stark");
    drawString(5, 8, WHITE, m);
        
    sprintf(m, "MECH_ENG 433");
    drawString(85, 8, WHITE, m);
        
    sprintf(m, "May 20, 2021");
    drawString(160, 8, WHITE, m);
        
    sprintf(m, "Homework 11");
    drawString(5, 24, WHITE, m);
    
    //_CP0_SET_COUNT(0);
    while (1) {
        _CP0_SET_COUNT(0);
                

        
        
        i2c_read_multiple(LSM6DS33_ADDRESS, OUT_TEMP_L, data, 14);
        
        
        int ii = 0;
        for (kk=0; kk<14; kk=kk+2) {
        
            newData[ii] = (data[kk] << 0) | (data[kk+1] << 8);
            
            ii = ii + 1;
        }
        
        
        newData[0] = (25 + (60*newData[0])/32767);
        
        //sprintf(m, "Temp  : %d", newData[0]);
        //drawString(5, 64, WHITE, m);
        
        sprintf(m, "FPS   : %d", FPS);
        drawString(160, 64, WHITE, m);
        
        //sprintf(m, "Gyro X: %d", newData[1]);
        //drawString(5, 80, WHITE, m);
        
        //sprintf(m, "Gyro Y: %d", newData[2]);
        //drawString(85, 80, WHITE, m);
        
        //sprintf(m, "Gyro Z: %d", newData[3]);
        //drawString(160, 80, WHITE, m);
        
        //sprintf(m, "Acc  X: %d", newData[4]);
        //drawString(5, 96, WHITE, m);
        
        //sprintf(m, "Acc  Y: %d", newData[5]);
        //drawString(85, 96, WHITE, m);
        
        //sprintf(m, "Acc  Z: %d", newData[6]);
        //drawString(160, 96, WHITE, m);
        
        
        bar_x(newData[5]);
        bar_y(-1 * newData[4]);
        
        
        FPS = (48000000/2) / _CP0_GET_COUNT();
    }
}


