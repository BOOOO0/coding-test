package com.company.string;

import java.util.*;

public class ReverseOnlyAlphabet {
    public static String solution(String str){
        String answer;
        char[] arr = str.toCharArray();
        char tmp;

        int lt = 0 ,rt = str.length()-1;

        while(lt<rt){
            if(!Character.isAlphabetic(arr[lt])){
                lt++;
            } else if(!Character.isAlphabetic(arr[rt])){
                rt--;
            } else{
                tmp = arr[rt];
                arr[rt] = arr[lt];
                arr[lt] = tmp;
                lt++;
                rt--;
            }
        }
        answer = String.valueOf(arr);
        return answer;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        System.out.println(solution(str));
    }
}
