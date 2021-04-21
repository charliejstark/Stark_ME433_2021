#include<xc.h>           // processor SFR definitions
#include<sys/attribs.h>  // __ISR macro
#include<stdio.h>
#include "NU32.h"

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
    LATAbits.LATA4 = 0;
    
    U1RXRbits.U1RXR = 0b0001;   // RB6
    RPB7Rbits.RPB7R = 0b0001;   // RB7
    
    // HW5
    NU32_Startup();
    
    
    __builtin_enable_interrupts(); // enable interrupts after initializing things

    char m[100];
    
    while (1) {
        // use _CP0_SET_COUNT(0) and _CP0_GET_COUNT() to test the PIC timing
        // remember the core timer runs at half the sysclk

        // If condition checks if B4 is LOW (checks if button is pushed)
        if (PORTBbits.RB4 == 0) {
            
            _CP0_SET_COUNT(0);  // Sets timer to 0
            LATAbits.LATA4 = 1; // First blink begins at time = 0 [s]
            
            while (_CP0_GET_COUNT() < 12000000) {;} // Wait until time = 0.5 [s]
            LATAbits.LATA4 = 0; // First blink ends at time = 0.5 [s]
            
            while (_CP0_GET_COUNT() < 24000000) {;} // Wait until time = 1 [s]
            LATAbits.LATA4 = 1; // Second blink begins at time = 1 [s]

            while (_CP0_GET_COUNT() < 36000000) {;} // Wait until time = 1.5 [s]
            LATAbits.LATA4 = 0; // Second blink ends at time = 1.5 [s]
            
            while (_CP0_GET_COUNT() < 48000000) {;} // Wait until time = 2 [s]
            // Return to while(1) loop. Will check then if button is still pushed - repeats if so.
            
            sprintf(m, "Hello!\t");
            writeUART1(m);
            
        }
    }
}