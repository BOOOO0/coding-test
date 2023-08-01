package com.company.string;

public class CaseChange {
    static String str = "StuDY";

    public static void main(String[] args) {
        System.out.println(solution(str));
    }
    public static String solution(String str){
        StringBuilder answer = new StringBuilder();
        char[] arr = str.toCharArray();

        for(char ch : arr){
            if((int) ch >= 65 && (int) ch <= 97) {
                ch = (char) ((int) ch + 32);
            } else
                ch = (char) ((int) ch - 32);
            answer.append(ch);
        }

        return answer.toString();
    }
}
