| **效果**               | **LaTeX 代码**          | **说明**             |
| -------------------- | --------------------- | ------------------ |
| $\rightarrow$        | `\rightarrow` 或 `\to` | 标准右箭头              |
| $\longrightarrow$    | `\longrightarrow`     | 长右箭头               |
| $\Rightarrow$        | `\Rightarrow`         | 双线右箭头（通常表示“推出”）    |
| $\Longrightarrow$    | `\Longrightarrow`     | 长双线右箭头             |
| $\hookrightarrow$    | `\hookrightarrow`     | 带钩右箭头（常用于数学中的包含映射） |
| $\rightleftharpoons$ | `\rightleftharpoons`  | 正逆反应双箭头（化学常用）      |

| **需求**    | **语法 (Obsidian 中输入)**                | **渲染效果**                       |
| --------- | ------------------------------------ | ------------------------------ |
| **单元素**   | `$\ce{O}$`, `$\ce{Fe}$`, `$\ce{Cu}$` | $\ce{O}$, $\ce{Fe}$, $\ce{Cu}$ |
| **普通化学式** | `$\ce{H2O}$`, `$\ce{CO2}$`           | $\ce{H2O}$, $\ce{CO2}$         |
| **复杂化学式** | `$\ce{H2SO4}$`, `$\ce{Ca(OH)2}$`     | $\ce{H2SO4}$, $\ce{Ca(OH)2}$   |
| **带结晶水**  | `$\ce{CuSO4 . 5H2O}$` (注意点号前后有空格)    | $\ce{CuSO4 . 5H2O}$            |
|           |                                      |                                |

### 1. 关系与比较运算符

| **效果**        | **LaTeX 代码**   | **说明**          |
| ------------- | -------------- | --------------- |
| $\ne$         | `\ne` 或 `\neq` | 不等于             |
| $\approx$     | `\approx`      | 约等于             |
| $\le$ / $\ge$ | `\le` / `\ge`  | 小于等于 / 大于等于     |
| $\sim$        | `\sim`         | 相似于 / 按比例 / 渐近于 |
| $\propto$     | `\propto`      | 正比于 (电离、电路分析常客) |
| $\equiv$      | `\equiv`       | 恒等于 / 同余        |

---

### 2. 算术与集合运算符

|**效果**|**LaTeX 代码**|**说明**|
|---|---|---|
|$\pm$ / $\mp$|`\pm` / `\mp`|正负号 / 负正号|
|$\times$ / $\div$|`\times` / `\div`|乘号 / 除号|
|$\cdot$|`\cdot`|点乘 (如向量点积 $A \cdot B$)|
|$\in$ / $\notin$|`\in` / `\notin`|属于 / 不属于|
|$\subset$ / $\subseteq$|`\subset` / `\subseteq`|包含于 (真子集 / 子集)|
|$\cap$ / $\cup$|`\cap` / `\cup`|交集 / 并集|
|$\varnothing$|`\varnothing` 或 `\emptyset`|空集|

---

### 3. 高等数学与逻辑符号

对于更复杂的公式（如微积分、场论或逻辑推理），以下符号非常高频：

|**效果**|**LaTeX 代码**|**说明**|
|---|---|---|
|$\infty$|`\infty`|无穷大|
|$\partial$|`\partial`|偏微分符号|
|$\nabla$|`\nabla`|算子 / 梯度 / 旋度符号|
|$\int$ / $\iint$|`\int` / `\iint`|单重积分 / 双重积分|
|$\sum$ / $\prod$|`\sum` / `\prod`|求和号 / 求积号|
|$\because$ / $\therefore$|`\because` / `\therefore`|因为 / 所以|
|$\forall$ / $\exists$|`\forall` / `\exists`|任意 / 存在|

> 💡 **小提示**：如果想给积分号或求和号加上下限，只需配合下划线 `_` 和上标 `^`。
> 
> 例如：`$\int_0^\infty$` 渲染为 $\int_0^\infty$ ；`$\sum_{i=1}^n$` 渲染为 $\sum_{i=1}^n$。

---

### 4. 常用希腊字母

希腊字母在公式中通常作变量或参数，**首字母大写代码会得到大写字母**：

| **小写效果**  | **代码**    | **大写效果**  | **代码**    | **常用场景示例**   |
| --------- | --------- | --------- | --------- | ------------ |
| $\alpha$  | `\alpha`  | $A$       | `A`       | 角度、衰减常数      |
| $\beta$   | `\beta`   | $B$       | `B`       | 角度、相位常数      |
| $\gamma$  | `\gamma`  | $\Gamma$  | `\Gamma`  | 增益、反射系数      |
| $\delta$  | `\delta`  | $\Delta$  | `\Delta`  | 微量 / 变化量（大写） |
| $\theta$  | `\theta`  | $\Theta$  | `\Theta`  | 角度、功角        |
| $\lambda$ | `\lambda` | $\Lambda$ | `\Lambda` | 波长、特征值       |
| $\pi$     | `\pi`     | $\Pi$     | `\Pi`     | 圆周率          |
| $\omega$  | `\omega`  | $\Omega$  | `\Omega`  | 角频率 / 欧姆（大写） |

---

### 5. 修饰符号（向量与相量）

在写工程或物理公式时，经常需要给字母加个“帽子”：

- **普通向量**：`$\vec{a}$` $\rightarrow$ $\vec{a}$
    
- **长向量**：`$\vec{AB}$` 会显得箭头太小，推荐用 `$\overrightarrow{AB}$` $\rightarrow$ $\overrightarrow{AB}$
    
- **单位向量/估算值（尖帽子）**：`$\hat{x}$` $\rightarrow$ $\hat{x}$
    
- **平均值/共轭（横线）**：`$\overline{X}$` $\rightarrow$ $\overline{X}$
    
- **相量/点乘（加点）**：`$\dot{I}$` 或 `$\dot{U}$` $\rightarrow$ $\dot{I}$, $\dot{U}$


在 LaTeX 中，分式使用 `\frac{分子}{分母}` 命令。

- **基础语法**：`$\frac{1}{2}$` $\rightarrow$ $\frac{1}{2}$
    
- **复杂公式示例**：
    
    Markdown
    
    ```
    $$I = \frac{U}{R}$$
    ```
    
    > **效果：**
    > 
    > $$I = \frac{U}{R}$$
    

💡 **进阶小提示**：

如果在行内公式里，`\frac` 会为了适应行高而自动缩小（变成 $\frac{a}{b}$）。如果你希望它在行内也能保持正常大小，可以使用 `\dfrac`：

- 行内正常大小：`$\dfrac{U}{R}$` $\rightarrow$ $\dfrac{U}{R}$


| **符号**   | **规范写法 (LaTeX)**                                           | **错误写法**      | **为什么要用正体**              |
| -------- | ---------------------------------------------------------- | ------------- | ------------------------ |
| **微分号**  | `$\mathrm{d}x$` $\rightarrow$ $\mathrm{d}x$                | $dx$          | 它是算子，不是变量 $d$            |
| **虚数单位** | `$\mathrm{j}$` 或 `$\mathrm{i}$` $\rightarrow$ $\mathrm{j}$ | $j$           | 它是固定常量，避免和电流密度或电流 $j$ 混淆 |
| **自然底数** | `$\mathrm{e}^{x}$` $\rightarrow$ $\mathrm{e}^{x}$          | $e^x$         | 它是常量，避免和电子电荷量 $e$ 混淆     |
| **物理单位** | `$50\text{ Hz}$`, `$10\text{ A}$`                          | $50Hz$, $10A$ | 所有的物理单位（安培、赫兹、欧姆）必须是正体   |
### 分段函数/条件分支的“单边大巨型左大括号”

如果你想写一个分段函数，或者在推导电力系统、电路方程时，左边需要一个巨大的单侧大括号，右边分成好几行，**千万不要手动去对齐**，请直接使用 `cases` 环境：

Markdown

```
$$
\begin{cases}
U = IR \\
P = UI \\
W = Pt
\end{cases}
$$
```

> **效果：**
> 
> $$\begin{cases} U = IR \\ P = UI \\ W = Pt \end{cases}$$

_(注：在 `cases` 环境里，每一行末尾用双反斜杠 `\\` 表示换行，它会自动帮你把左侧的单边大括号撑大。)_

### 2. 极坐标形式 / 极角流派（写具体数值最常用：$220 \angle 30^\circ$）

当你需要写出相量的**模长**和**初相角**时，需要用到那个像漏斗一样的“角符号”。

- **实现方法**：使用 `\angle` 命令表示角度，使用 `^\circ` 表示右上角的度数圆圈。
    
- **示例代码**：
    

Markdown

````
    $\dot{U} = 220 \angle 30^\circ \text{ V}$
    ```
*   **渲染效果**：$\dot{U} = 220 \angle 30^\circ \text{ V}$

---

### 3. 粗体/矢量流派（国际标准与英文教材常用：$\mathbf{U}$ 或 $\vec{U}$）

在很多外文原版教材或者国际 IEEE 论文中，相量不加点，而是使用**加粗的正体**（Bold Roman）或者**加箭头**来表示复数矢量。

*   **加粗正体**：使用 `\mathbf{}`
    *   代码：`$\mathbf{U}$` $\rightarrow$ $\mathbf{U}$
*   **加小箭头**：使用 `\vec{}`
    *   代码：`$\vec{U}$` $\rightarrow$ $\vec{U}$

---

### 综合实战演练

把它们组合在一起，在 Obsidian 里写一段完美的正弦稳态电路分析笔记：

```markdown
已知某感性负载的阻抗为 $Z = 3 + \mathrm{j}4 \, \Omega$，通入电流相量 $\dot{I} = 10 \angle 0^\circ \text{ A}$。

则负载两端的电压相量为：
$$
\dot{U} = \dot{I} \cdot Z = 10 \angle 0^\circ \times 5 \angle 53.13^\circ = 50 \angle 53.13^\circ \text{ V}
$$
````

> **渲染效果：**
> 
> 已知某感性负载的阻抗为 $Z = 3 + \mathrm{j}4 \, \Omega$，通入电流相量 $\dot{I} = 10 \angle 0^\circ \text{ A}$。
> 
> 则负载两端的电压相量为：
> 
> $$\dot{U} = \dot{I} \cdot Z = 10 \angle 0^\circ \times 5 \angle 53.13^\circ = 50 \angle 53.13^\circ \text{ V}$$

_(注：这里的虚数单位 $\mathrm{j}$ 和单位 $\Omega$、$\text{V}$，我们都规范地使用了正体。)_