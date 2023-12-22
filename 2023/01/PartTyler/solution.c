#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>

int main(){

    FILE *myFile;
    myFile = fopen("message.txt","r");

    char numberArray[54];
    int i;
    int j;
    char firstDigit;
    char lastDigit;
    int flag = 0;
    int total;
    int sum = 0;

    if(myFile == NULL){
        printf("Error Reading File\n");
        exit (0);
    }

    for(j=0; j<1000; j++){
        flag = 0;
        for(i=0; i < 60; i++){
            fscanf(myFile, "%c", &numberArray[i]);
        //}
        //for (i=0; i < 54; i++){
            if(numberArray[i] == '\n'){
                break;
            }
            printf("Value is: %c\n", numberArray[i]);
            if(isdigit(numberArray[i]) > 0){
                printf("Number is: %c\n", numberArray[i]);
                /*if(isspace(numberArray[i]) != 0){
                }*/

                if(flag == 0){
                    firstDigit = numberArray[i];
                    printf("First Digit updated: %c\n\n", firstDigit);
                    lastDigit = numberArray[i];
                    printf("Last Digit updated: %c\n\n", lastDigit);
                    flag = 1;
                }
                if(flag == 1){
                    lastDigit = numberArray[i];
                    printf("Last Digit updated: %c\n\n", lastDigit);
                }
            }
        }
        printf("First Digit is: %c\n\n", firstDigit);
        printf("Last Digit is: %c\n\n", lastDigit);
        total = ((firstDigit - '0')*10) + (lastDigit - '0');
        printf("This line's total is: %d\n\n", total);
        sum = sum + total;
        printf("This is the current sum: %d\n\n", sum);
    }
    printf("The total digit is: %d\n\n", sum);
    fclose(myFile);
    return 0;
}