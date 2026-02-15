# Employee Burnout Analysis & Prediction  

## What If Burnout Could Be Predicted Before It Happens?

What if employee burnout was not something organizations *reacted* to—but something they could **measure, model, and prevent**?

This project treats burnout as a **data problem**, not a mystery. Using measurable work-behavior variables—work hours, screen time, meetings, sleep, breaks, and after-hours activity—it analyzes how daily patterns **systematically increase or reduce burnout risk**.

Through **data visualization** and **machine learning**, this repository identifies the strongest drivers of burnout and builds predictive models that estimate:

- **Burnout Risk** (`Low`, `Medium`, `High`)
- **Burnout Score** (continuous intensity measure)

The goal is simple and factual: **detect burnout early using data, before performance and well-being collapse**.



##  End-to-End Data Flow

This project follows a structured **data flow pipeline**, where raw employee activity data is progressively transformed into actionable burnout predictions.

---

## 1️ Raw Data Ingestion

The process starts with a raw dataset containing daily employee work behavior and wellness indicators.

**Input data includes:**
- Work intensity metrics (work hours, meetings, screen time)
- Recovery metrics (breaks taken, sleep hours)
- Behavioral signals (after-hours work)
- Performance signal (task completion rate)
- Context variable (day type)

At this stage:
- Data is unmodified
- No assumptions are applied
- Values reflect real observed behavior

---

## 2️ Categorical-to-Numerical Transformation

Machine learning models require numerical inputs.

Two categorical variables are transformed into numeric representations:
- `day_type`
- `burnout_risk`

This step converts human-readable categories into model-consumable signals while preserving their ordering.

---

## 3️ Feature Matrix Construction

The dataset is divided into:
- **Input features (X)** – employee behavior and context
- **Target variables (y)** – burnout outcomes

Excluded from features:
- Unique identifiers
- Burnout labels and scores

This ensures:
- No data leakage
- Fair model learning

---

## 4️ Feature Normalization

All input features are scaled to a common range.

**Why this matters:**
- Prevents dominance of large-scale values
- Stabilizes learning for linear models
- Improves comparability across variables

After this step:
- Each feature contributes proportionally
- Patterns reflect relationships, not magnitudes

---

## 5️ Target Separation

The data flow branches into **two parallel prediction paths**:

### 🔹 Path A: Burnout Risk (Classification)
- Output: `Low`, `Medium`, `High`
- Purpose: Identify employees at risk

### 🔹 Path B: Burnout Score (Regression)
- Output: Continuous value
- Purpose: Measure burnout intensity

This dual-path design allows both **early warning** and **severity estimation**.

---

## 6️ Train–Test Partitioning

Data is split into:
- Training set (75%)
- Testing set (25%)

This simulates real-world deployment where models predict unseen data.

---

## 7️ Model Learning Phase

### Regression Flow
- Models learn relationships between work patterns and burnout score
- Linear and non-linear relationships are captured

### Classification Flow
- Models learn boundaries between burnout risk levels
- Decision rules are formed from behavioral signals

---

## 8️ Prediction Generation

Trained models produce:
- Burnout risk labels
- Burnout score estimates

Predictions are generated exclusively on unseen test data.

---

## 9️ Performance Evaluation

Predictions are compared against actual outcomes using:
- Accuracy for risk classification
- R² score for burnout score prediction

This quantifies how well the data explains burnout.

---

##  Insight Extraction

Model outputs are analyzed to determine:
- Which variables increase burnout risk
- Which behaviors reduce burnout
- How strongly each feature influences outcomes

Tree-based models provide feature importance scores for interpretability.

---

## Final Data Output

The final outputs of the data flow are:
- Predicted burnout risk levels
- Predicted burnout scores
- Ranked burnout drivers

These outputs can be used for:
- Early intervention
- Policy design
- Workload optimization
- Employee well-being monitoring

---

## Data Flow Summary

**Raw Employee Data → Encoded Data → Normalized Features →  
Train/Test Split → Model Learning → Predictions → Insights**

This pipeline converts everyday work behavior into **measurable burnout intelligence**.



## Linear Regression Results Interpretation

### Model Context
- **Target variable:** Burnout Score (continuous)
- **Model:** Linear Regression
- **Features:** Standardized (coefficients are directly comparable)

---

###  Feature-wise Coefficient Interpretation

| Feature | Coefficient | Interpretation |
|------|------------|---------------|
| **work_hours** | -0.43 | Increasing work hours slightly **reduces burnout score** when other variables are constant. Workload alone is not a primary burnout driver. |
| **screen_time_hours** | +0.53 | Higher screen time **increases burnout**. Prolonged digital exposure contributes directly to burnout. |
| **meetings_count** | -0.14 | More meetings slightly **reduce burnout**, possibly reflecting coordination or support. The effect is weak. |
| **breaks_taken** | +0.19 | More breaks correlate with **higher burnout**, suggesting breaks are taken as a response to burnout rather than a cause. |
| **after_hours_work** | -0.35 | After-hours work slightly **reduces burnout score** in isolation, indicating flexible or voluntary work patterns. |
| **sleep_hours** | +0.22 | Higher sleep duration is associated with **higher burnout**, likely reflecting recovery behavior. |
| **task_completion_rate** | **-22.93** | **Strongest effect in the model.** Higher task completion dramatically **reduces burnout score**. Productivity is the key protective factor. |
| **day_type** | ~0.00 | Day type (weekday vs weekend) has **no meaningful impact** on burnout score. |

---

###  Intercept Interpretation

**Intercept = 44.01**

This represents the **baseline burnout score** when all standardized features are at their mean values.  
An average employee starts at a **moderate burnout level**, which then shifts based on behavior patterns.

---

###  Key Insights

- **Task completion rate dominates burnout prediction**
- **Screen time matters more than total work hours**
- **Burnout reflects efficiency and digital strain, not just workload**
- **Some variables represent coping behavior rather than causes**
- **Calendar effects are negligible**

---

### Summary

> Burnout is driven more by **how work is performed** than **how long work is performed**.  
> Productivity and screen exposure explain burnout better than hours worked.


## Random Forest Feature Importance Interpretation

Random Forest models capture **non-linear effects and feature interactions**.  
Feature importance values represent how much each variable contributes to prediction accuracy.

---

## Random Forest Regressor  
**Target:** Burnout Score (continuous)

| Feature | Importance | Interpretation |
|------|-----------|---------------|
| **task_completion_rate** | **94.46** | **Overwhelmingly dominant factor.** Burnout severity is primarily explained by productivity loss. |
| **sleep_hours** | 1.48 | Secondary contributor. Sleep patterns influence burnout intensity but far less than productivity. |
| **work_hours** | 1.45 | Workload has a measurable but limited effect on burnout score. |
| **screen_time_hours** | 1.44 | Digital exposure contributes modestly to burnout severity. |
| **meetings_count** | 0.55 | Minor influence. Meetings alone do not drive burnout score. |
| **breaks_taken** | 0.47 | Low impact. Breaks reflect coping rather than cause. |
| **after_hours_work** | 0.16 | Minimal contribution to burnout intensity. |
| **day_type** | ~0.00 | No predictive value for burnout score. |

### Key Insight (Regression)
> **Burnout severity is almost entirely explained by task completion rate.**  
> When productivity collapses, burnout score rises sharply—other variables play supporting roles.

---

## Random Forest Classifier  
**Target:** Burnout Risk Level (Low / Medium / High)

| Feature | Importance | Interpretation |
|------|-----------|---------------|
| **day_type** | **60.88** | **Strongest signal for burnout risk.** Burnout risk differs significantly between weekdays and weekends. |
| **screen_time_hours** | 8.44 | High screen exposure strongly increases burnout risk. |
| **sleep_hours** | 8.24 | Sleep duration is a key indicator of burnout risk. |
| **after_hours_work** | 8.13 | Consistent after-hours work meaningfully raises burnout risk. |
| **work_hours** | 7.94 | Long working hours increase likelihood of burnout. |
| **meetings_count** | 3.09 | Moderate contributor to burnout risk. |
| **breaks_taken** | 2.44 | Weak-to-moderate signal, often reactive rather than causal. |
| **task_completion_rate** | 0.84 | Minimal role in predicting burnout risk level. |

### Key Insight (Classification)
> **Burnout risk is driven by time structure and recovery failure**, not productivity.  
> Calendar effects, screen exposure, sleep, and after-hours work define risk.

---

# Regression vs Classification: What Changes?

| Aspect | Burnout Score (Regressor) | Burnout Risk (Classifier) |
|------|---------------------------|---------------------------|
| What it measures | Burnout severity | Burnout likelihood |
| Dominant factor | Task completion rate | Day type & recovery patterns |
| Nature of burnout | Performance collapse | Stress accumulation |
| Model focus | Output intensity | Early warning |

---

## Final Interpretation

- **Burnout severity** reflects **how badly performance has degraded**
- **Burnout risk** reflects **work structure, time pressure, and recovery**
- The same data reveals **different burnout mechanisms** depending on the target
- Random Forest exposes relationships that linear models cannot capture

> Burnout is not a single signal.  
> It has **distinct behavioral signatures for risk and severity**, and both must be modeled.




## 📊 Interactive Dashboard Insights

To complement the machine learning analysis, an interactive dashboard was developed to **visually validate patterns in the data**. The dashboard focuses on relationships that are most relevant for understanding burnout behavior.

---

## 🔹 Burnout Score vs Task Completion Rate (Scatter Plot)

**Observation:**
- A **strong negative relationship** is clearly visible
- As task completion rate increases, burnout score decreases sharply

**Interpretation:**
- Employees who consistently complete tasks experience significantly lower burnout
- Productivity is a **protective factor**, not a stressor
- This visual finding strongly supports both the **Linear Regression** and **Random Forest Regressor** results

> This is the most dominant relationship observed in the dashboard.

---

## 🔹 Average Work Hours vs Burnout Risk Level (Horizontal Bar Chart)

**Axes:**
- **X-axis:** Average number of working hours  
- **Y-axis:** Burnout risk level (`Low`, `Medium`, `High`)

**Observation:**
- No strong separation across burnout risk levels
- Distributions largely overlap
- A **slight increase in high burnout risk** is observed for employees working **more than 6 hours**

**Interpretation:**
- Long hours alone do not explain burnout
- Burnout emerges when long hours combine with other stressors
- This confirms that workload is a **secondary contributor**, not the main driver

---

## 🔹 Sleep Hours vs Burnout Score (Scatter Plot)

**Observation:**
- Very **weak correlation** between sleep hours and burnout score
- Points are widely scattered with no clear trend

**Interpretation:**
- Sleep duration alone does not predict burnout severity
- Sleep likely reflects recovery behavior rather than burnout cause
- This aligns with the weak importance of sleep in regression models

---

## 🔹 Number of Breaks vs Burnout Score

**Observation:**
- No significant relationship between breaks taken and burnout score
- Burnout levels remain similar regardless of break count

**Interpretation:**
- Taking more breaks does not automatically reduce burnout
- Breaks may be reactive rather than preventative
- Burnout depends more on **work structure and productivity** than short-term pauses

---

## 📌 Dashboard Summary

- **Strongest visual signal:** Task completion rate vs burnout score
- **Weak or negligible signals:** Sleep hours, breaks taken
- **Moderate signal:** Long work hours slightly increase burnout risk
- Visual analysis **confirms machine learning findings**

---

<img width="1132" height="839" alt="image" src="https://github.com/user-attachments/assets/728e55bf-8daa-45b9-974c-67e89ae64373" />



