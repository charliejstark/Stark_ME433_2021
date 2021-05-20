#include<xc.h>           // processor SFR definitions
#include<sys/attribs.h>  // __ISR macro
#include<stdio.h>
#include "spi.h"
#include<math.h>

#include "ST7789.h"
#include "font.h"

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
    
    // HW7
    initSPI();
    LCD_init();
    
    __builtin_enable_interrupts(); // enable interrupts after initializing things

    char M[50];
    LCD_clearScreen(BLACK);
    
    //progressBar(5, 72, 100, WHITE);
    //unsigned short progress = 0;
    
    _CP0_SET_COUNT(0);
    double FPS = 0;
    double oneSecond = 48000000 / 2;
    
    while (1) {
        LCD_clearScreen(BLACK);
        _CP0_SET_COUNT(0);
        //if (_CP0_GET_COUNT() > (48000000 / 2 / 10)) {
        //    _CP0_SET_COUNT(0);
            
        //    progress = progress + 1;
            
        //    sprintf(m, "Charles Stark");
        //    drawString(5, 8, WHITE, m);

        //    sprintf(m, "MECH_ENG 433");
        //    drawString(80, 8, WHITE, m);

        //    sprintf(m, "May 18, 2021");
        //    drawString(160, 8, WHITE, m);

        //    sprintf(m, "Hello world %d!    ", progress);
        //    drawString(28, 32, WHITE, m);

        //    sprintf(m, "FPS: %d Hz    ", FPS);
        //    drawString(28, 44, WHITE, m);

        //    sprintf(m, "Progress:");
        //    drawString(5, 64, WHITE, m);

        //    progressBar(5, 72, progress, BLUE);

        //    FPS = (48000000 / 2) / _CP0_GET_COUNT();

 
        //}
        
        //if (progress > 100) {
        //    progress = 0;
        //    progressBar(5, 72, 100, WHITE);
        //}
        
        sprintf(M, "FPS: %f                                ", FPS);
        drawString(0, 0, WHITE, M);
        
        sprintf(M, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
        unsigned short jj;
        for (jj=8; jj<240; jj=jj+8) {
            drawString(0,jj,WHITE,M);
        }
        
        
        
        
        FPS = oneSecond / _CP0_GET_COUNT();
    }
}