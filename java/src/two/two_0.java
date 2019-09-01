package two;

public class two_0 {
    public class ListNode {
        int val;
        ListNode next;
        ListNode(int x) {val = x;}
    }
    public ListNode addTwoNumbers(ListNode l1,ListNode l2){
        ListNode pre = new ListNode(0); //设置一个预先指针
        ListNode cur = pre; //当前头指针
        int carry = 0; //控制进位

        while(l1 != null || l2 != null) {
            int x = l1 == null ? 0 : l1.val;
            int y = l2 == null ? 0 : l2.val;
            int sum = x + y + carry;

            carry = sum / 10; //得到进位
            sum = sum % 10; //取余
            cur.next = new ListNode(sum); //将计算出的和放入链表

            cur = cur.next;
            if(l1 != null)
                l1 = l1.next;
            if(l2 != null)
                l2 = l2.next;
        }
        if(carry == 1){
            cur.next = new ListNode(carry);
        } //最后还多一位
        return pre.next;
    }
}

