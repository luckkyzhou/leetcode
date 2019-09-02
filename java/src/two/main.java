package two;

public class main {

    public static void main(String[] args){
        two_0.ListNode l1 = new two_0.ListNode(7);
        two_0.ListNode cur = l1;
        l1.next = new two_0.ListNode(8);
        l1 = l1.next;
        l1.next = new two_0.ListNode(9);
        System.out.println(l1);
    }
}
