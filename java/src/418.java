class Solution {
    public int wordsTyping(String[] sentence, int rows, int cols) {
        int len = sentence.length;
        int result = 0;
        int curr = 0;
        int idx = 0;
        int l = 0;
        for (String s : sentence) {
            l = l + s.length()+1;
        }
        for (int i = 0; i < rows; i++) {
            curr = cols;
            while (curr > 0 && curr >= sentence[idx].length()) {
                curr = curr - sentence[idx].length();
                idx++;
                if (curr > 0) {
                    curr--;
                }
                if (idx == len) {
                    result += curr / l+1;
                    curr = curr % l;
                    idx = 0;

                }

            }
        }
        return result;
    }
}