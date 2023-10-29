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


// Sum Tree 
pair<bool, int> isSumTreeFast(Node* root) {
    if(root == nullptr) return make_pair(true, 0);

    if(root->left == nullptr && root->right == nullptr)
        return make_pair(true, root->data);

    pair<bool, int> left = isSumTreeFast(root->left);
    pair<bool, int> right = isSumTreeFast(root->right);

    pair<bool, int> ans = make_pair(false, 0);

    if(left.first && right.first && root->data == left.second + right.second)
        ans = make_pair(true, 2 * root->data);

    return ans;
}

bool isSumTree(Node* root) {
    return isSumTreeFast(root).first;
}



// Transform to Sum Tree
int solve(TreeNode* root) {
    if(root == nullptr) return 0;

    int left = solve(root->left);
    int right = solve(root->right);
    int data = root->val;
    root->val = left + right;
    return data + left + right;
}

void toSumTree(TreeNode* root) {
    solve(root);
    return;
}



// 112. Path Sum 
// DFS Approach 
bool hasPathSum(TreeNode* root, int targetSum) {
    if(root == nullptr)
        return false;

    targetSum -= root->val;

    if(root->left == nullptr && root->right == nullptr)
        return targetSum == 0;

    bool left = hasPathSum(root->left, targetSum);
    bool right = hasPathSum(root->right, targetSum);

    return left || right;
}


// 113. Path Sum II 
void checkSum(TreeNode* root, int k, vector<int>& currPath, vector<vector<int>>& res) {
    if(root == nullptr) return;

    currPath.push_back(root->val);

    if(root->left == nullptr && root->right == nullptr) {
        if(root->val == k) {
            res.push_back(currPath);
        } 
    } else {
        checkSum(root->left, k - root->val, currPath, res);
        checkSum(root->right, k - root->val, currPath, res);
    }
    currPath.pop_back();
}

vector<vector<int>> pathSum(TreeNode* root, int k) {
    vector<vector<int>> res;
    vector<int> currPath;
    checkSum(root, k, currPath, res);
    return res;
}


// 437. Path Sum III
int solve(TreeNode* root, int k, long long currSum, unordered_map<long long, int>& map) {
    if(root == nullptr) return 0;

    currSum += root->val;
    int cnt = 0;
    if(map.find(currSum - k) != map.end()) {
        cnt += map[currSum - k];
    }

    map[currSum]++;
    int left = solve(root->left, k, currSum, map);
    int right = solve(root->right, k, currSum, map);
    map[currSum]--;

    return left + right + cnt;
}

int pathSum(TreeNode* root, int k) {
    unordered_map<long long, int> map;
    map[0] = 1;
    return solve(root, k, 0LL, map);
}


// 687. Longest Univalue Path 
int path(TreeNode* root, int& ans, int prev = -1) {
    if(root == nullptr) return 0;

    int left = path(root->left, ans, root->val);
    int right = path(root->right, ans, root->val);

    ans = max(ans, left + right);

    if(root->val != prev) return 0;

    return max(left, right) + 1;
}

int longestUnivaluePath(TreeNode* root) {
    int ans = 0;
    path(root, ans);
    return ans;
}


// Binary Tree Maximum Path Sum 




