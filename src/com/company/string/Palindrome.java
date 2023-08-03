package com.company.string;

import java.util.*;

public class Palindrome {
    static String solution(String str){
        str = str.toLowerCase();
        char[] arr = str.toCharArray();
        int lt=0,rt=arr.length-1;

        while(lt<rt){
            if(Objects.equals(arr[lt], arr[rt])){
                lt++;
                rt--;
            }else{
                return "NO";
            }
        }
        return "YES";
    }
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        String str=kb.next();
        System.out.print(solution(str));
    }
}
