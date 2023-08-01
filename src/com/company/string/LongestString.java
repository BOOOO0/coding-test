package com.company.string;

import static java.lang.Integer.*;

public class LongestString {
    static String str = "it is time to study";

    public static void main(String[] args) {
        System.out.println(solution(str));
    }
    static String solution(String str){
        String answer = "";
        int max = Integer.MIN_VALUE;
        String[] arr = str.split(" ");

        for(String s : arr){
            if(s.length() > max){
                max = s.length();
                answer = s;
            }
        }
        return answer;
    }
}
