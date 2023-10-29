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


// Root to Leaf Paths 
void inOrder(TreeNode* root, vector<int> &temp, vector<vector<int>> &ans){
    if(root == NULL) return;

    temp.push_back(root->val);
    inOrder(root->left, temp, ans);
    inOrder(root->right, temp, ans);

    if(root->right == NULL && root->left == NULL)
        ans.push_back(temp);
    temp.pop_back();
}

vector<vector<int>> Paths(TreeNode* root){
    vector<vector<int>> ans;
    vector<int> temp;
    inOrder(root,temp,ans);
    return ans;
}




// Root to leaf path sum
bool solve(TreeNode* root, int sum, int s){
    if(root == NULL) return false;
    sum += root->val;
    if(root->left == NULL and root->right == NULL) {
        if(sum == s) return true;
    }
    return solve(root->left, sum, s) || solve(root->right, sum, s);
}

bool hasPathSum(TreeNode *root, int S) {
    int sum=0;
    return solve(root, sum, S);
}




// 129. Sum Root to Leaf Numbers (Morris Traversal Possible)
// DFS Approch (Best Approach)
int total;
void preOrder(TreeNode* root, int sum) {
    if(root == nullptr) return;

    sum = sum * 10 + root->val;
    if(root->left == nullptr && root->right == nullptr) {
        total += sum;
        return;
    }

    preOrder(root->left, sum);
    preOrder(root->right, sum);
}

int sumNumbers(TreeNode* root) {
    total = 0;
    preOrder(root, total);
    return total;
}


// Another Approach
int solve(TreeNode* root, int currSum) {
    if(root == nullptr) return 0;
    currSum = currSum * 10 + root->val;

    if(root->left == nullptr && root->right == nullptr)
        return currSum;
    
    int left = solve(root->left, currSum);
    int right = solve(root->right, currSum);

    return left + right;
}

int sumNumbers(TreeNode* root) {
    int currSum = 0;
    return solve(root, currSum);
}


// BFS Approach 
int sumNumbers(TreeNode* root) {
    int sum = 0;
    queue<pair<TreeNode*, int>> qu; 
    qu.push(make_pair(root, 0)); 

    while (!qu.empty()) {
        pair<TreeNode*, int> temp = qu.front();
        qu.pop();
        TreeNode* curr = temp.first;
        int n = temp.second * 10 + curr->val; 

        if (curr->left) 
            qu.push(make_pair(curr->left, n));

        if (curr->right) 
            qu.push(make_pair(curr->right, n));

        if (!curr->left && !curr->right) 
            sum += n;
    }
    return sum;
}







// Duplicate subtree in Binary Tree