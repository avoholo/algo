public class Main {

    public int solution(String[] babbling) {
        int answer = 0;
        String[] babble_sets = {"aya", "ye", "woo", "ma"};
        for (int x=0; x < babbling.length; x++) {
            for (int y = 0; y < babble_sets.length; y++) {
                if (babbling[x].contains(babble_sets[y])) {
                    babbling[x] = babbling[x].replace(babble_sets[y], "*");
                }
            } if (babbling[x].matches(".*[a-zA-Z].*") == false) {
                answer++;
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        Main obj = new Main();
        String[] test = {"ayaye", "uuuma", "ye", "yemawoo", "ayaa"};
        System.out.println(obj.solution(test));
    }
}