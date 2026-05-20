class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        HashMap<Character, Character> closing = new HashMap<>();

        closing.put(')', '(');
        closing.put(']', '[');
        closing.put('}', '{');

        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            }
            else {
                if (stack.isEmpty() ||closing.get(c) != stack.peek() ) {
                    return false;
                }
                stack.pop();
            }
    
        }
        return stack.isEmpty();

        
    }
}
