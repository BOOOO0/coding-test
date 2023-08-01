package com.company.string;

import java.util.*;

public class FindChar {
    static String str = "Computercooler";
    static char c = 'c';

    public static void main(String[] args) {
        System.out.println(solution(str, c));
    }

    public static int solution(String str, char c){
        int answer = 0;
        str = str.toLowerCase();
        char[] arr  = str.toCharArray();

        for(char ch : arr){
            if(Objects.equals(ch, c)) {
                answer += 1;
            }
        }
        return answer;
    }
}
