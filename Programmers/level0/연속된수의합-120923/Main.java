public class Main {

    public int[] solution(int num, int total) {
        int[] answer = new int[num];

        int iter = 0;
        int div = total / num;
        int start = div - ((num - 1) / 2);
        int end = div + ((num + 2) / 2);
        for(int i = start; i < end; i++) {
            answer[iter] = i;
            iter++;
        }
        return answer;
    }

    public static void main(String[] args) {
        Main obj = new Main();
        int[] arr = obj.solution(5,5);
        for (int el : arr) {
            System.out.println(el);
        }
    }
}