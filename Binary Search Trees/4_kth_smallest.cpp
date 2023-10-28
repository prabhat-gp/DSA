// 230. Kth Smallest Element in a BST 
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int val) {
        this->val = val;
        this->left = NULL;
        this->right = NULL;
    }
}


int solve(TreeNode* root, int& i, int k) {
    if(root == nullptr) {
        return -1;
    }

    int left = solve(root->left, i, k);
    if(left != 1) {
        return left;
    }
    i++;
    if(i == k) {
        return root->val;
    }

    return solve(root->right, i, k);
}

int* kthSmallest(TreeNode* root, int k) {
    int i = 0;
    return solve(root, i, k);
}



// Kth Largest Element in BST = (n - k + 1)th smallest
int solve(TreeNode* root, int& i, int k) {
    if(root == nullptr) {
        return -1;
    }

    int right = solve(root->right, i, k);
    if(right != 1) {
        return right;
    }
    i++;
    if(i == k) {
        return root->val;
    }

    return solve(root->left, i, k);
}

int* kthLargest(TreeNode* root, int k) {
    int i = 0;
    return solve(root, i, k);
}


// Approach 2
void inorderTraversal(Node* root, vector<int> &ans) {
    if(root == nullptr) {
        return;
    }

    inorderTraversal(root->left, ans);
    ans.push_back(root->val);
    inorderTraversal(root->right, ans);
}

int KthSmallestElement(TreeNode *root, int k) {
    vector<int> ans;
    inorderTraversal(root,ans);

    if(ans.size() < k) {
        return -1;
    }
    
    return ans[k - 1];
}


// Optmised Approach (Morris Traversal) 

// 671. Second Minimum Node in a Binary Tree
// Approach 1 
void inorder(TreeNode* root, set<int> &ans) {
    if(root == nullptr) return;

    inorder(root->left, ans);
    ans.insert(root->val);
    inorder(root->right, ans);
}
int findSecondMinimumValue(TreeNode* root) {
    set<int> ans;
    inorder(root, ans);

    if (ans.size() < 2)
        return -1;

    int count = 0;
    int secondMinimum = -1;
    for (int value : ans) {
        if (count == 1) {
            secondMinimum = value;
            break;
        }
        count++;
    }
    return secondMinimum;
}


// Approach 2
int findSecondMinimumValue(TreeNode* root) {
    if (root == nullptr)
        return -1;
        
    int minVal = root->val;
    long secondMin = LLONG_MAX;  

    queue<TreeNode*> qu;
    qu.push(root);

    while (!qu.empty()) {
        TreeNode* curr = qu.front();
        qu.pop();

        if (curr->val != minVal) {
            secondMin = min(secondMin, (long)curr->val);
        }

        if (curr->left)
            qu.push(curr->left);
        if (curr->right)
            qu.push(curr->right);
    }
    return (secondMin == LLONG_MAX) ? -1 : (int)secondMin;
}