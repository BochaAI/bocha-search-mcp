[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/bochaai-bocha-search-mcp-badge.png)](https://mseep.ai/app/bochaai-bocha-search-mcp)

# MCP Server 产品名称: 博查

![Bocha Search MCP Server](assets/bocha-logo-720x180.png)

## 版本信息
v1

## 产品描述
### 短描述
博查是一个给AI用的搜索引擎，让你的AI应用从近百亿网页和生态内容源中获取高质量的世界知识，涵盖天气、新闻、百科、医疗、火车票、图片等多种领域。

### 长描述
博查是一个给AI用的搜索引擎，让你的AI应用从近百亿网页和生态内容源中获取高质量的世界知识，涵盖天气、新闻、百科、医疗、火车票、图片等多种领域。

## 分类
网页搜索

## 标签
搜索, 新闻, 天气, 百科

## Tools
### Tool1: Bocha Web Search
#### 详细描述
从博查搜索全网信息和网页链接，返回结果包括网页标题、网页URL、网页摘要、网站名称、网站图标、发布时间、图片链接等。

#### 调试所需要的参数
输入:
  - query: 搜索词(必填)
  - freshness: 搜索指定时间范围内的网页 (可选值 YYYY-MM-DD, YYYY-MM-DD..YYYY-MM-DD, noLimit, oneYear, oneMonth, oneWeek, oneDay. 默认为 noLimit)
  - count: 返回结果的条数 (1-50, 默认为 10)

输出:
  - 网页标题、网页链接、网页摘要、发布时间、网站名称

### Tool2: Bocha AI Search
#### 详细描述
在博查网页搜索的基础上，AI识别搜索词语义并额外返回垂直领域内容的结构化模态卡，例如天气卡、日历卡、百科卡等几十种模态卡，在语义识别、搜索结果时效性、内容丰富性等方面更好。

#### 调试所需要的参数
输入:
  - query: 搜索词(必填)
  - freshness: 搜索指定时间范围内的网页 (可选值 YYYY-MM-DD, YYYY-MM-DD..YYYY-MM-DD, noLimit, oneYear, oneMonth, oneWeek, oneDay. 默认为 noLimit)
  - count: 返回结果的条数 (1-50, 默认为 10)

输出:
  - 网页标题、网页链接、网页摘要、发布时间、网站名称、模态卡

## 可适配平台
方舟, python, Claude, Cursor等

## 服务开通链接
您需要前往 [博查AI开放平台](https://open.bochaai.com)，登陆后获取 API KEY。

## 鉴权方式
API Key

## 安装部署
### 步骤一：下载代码至本地
```bash
git clone git@github.com:BochaAI/bocha-search-mcp.git
```

### 步骤二: 在客户端中配置
#### Claude Desktop
On MacOS: `~/Library/Application\ Support/Claude/claude_desktop_config.json`

On Windows: `%APPDATA%/Claude/claude_desktop_config.json`

```json
  "mcpServers": {
    "bocha-search-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/bocha-search-mcp",
        "run",
        "bocha-search-mcp"
      ],
      "env": {
        "BOCHA_API_KEY": "sk-****"
      }
    }
  }
  ```

### 步骤三: 在客户端中使用
![示例: alibaba 2024 esg report](assets/alibaba-2024-esg-report.png)

### 步骤四: 调试本地服务（可选）
```bash
npx @modelcontextprotocol/inspector uv --directory /path/to/bocha-search-mcp run bocha-search-mcp
```

## 客户案例

目前博查已经累计服务**3000+企业用户**和**20000+开发者用户**，并且成为**DeepSeek官方联网搜索供应方**以及**阿里、腾讯、字节官方推荐的搜索API**，目前**承接着国内60%以上AI应用的联网搜索请求**。

博查的搜索内容源包括全网近百亿个网页，以及生态合作内容（含短视频、新闻、百科、天气、医疗、火车票、酒店、餐厅、景点、企业、学术等）。博查后续将会继续与各个平台在内容生态、智能体创作等方面开展共创合作，为博查用户的搜索问题提供丰富多彩的答案。

## 常见问题

### Bocha Web Search API服务可以提供什么样的能力?
Bocha Web Search 提供全网通用搜索能力。您可以从博查搜索全网信息和网页链接，返回结果包括网页标题、网页URL、网页摘要、网站名称、网站图标、发布时间、图片链接等，每次搜索结果返回的网页最多支持50条（count50）。

传统搜索引擎使用的是关键字+竞价排名机制的搜索算法，搜索结果的目标不是直接为用户提供正确的答案，而是吸引用户点击以获得广告收入。

博查是基于多模态混合搜索与语义排序技术的新一代搜索引擎，支持AI应用场景的自然语言搜索方式，同时搜索结果目标是提供干净、准确、高质量的答案。

博查的语义排序技术基于Transformer架构，会根据搜索结果与用户问题的语义相关性进行排序。由于大模型同样是Transformer架构，通过判断上下文与用户问题的语义相关性进行取舍，因此最终大模型更加喜欢博查提供的搜索结果。

目前博查的搜索效果是国内最接近Bing Search API的搜索引擎，由于Bing Search API数据会出海（无国内Region）、价格昂贵（15美元/千次）且不提供文本摘要（只有50-100字的snippet），国内很多企业客户都已经从Bing切换至博查。

### Bocha AI Search API 服务可以提供什么样的能力？
Bocha AI Search 在博查 Web Search 的基础上，AI识别搜索词语义并额外返回垂直领域内容的结构化模态卡，例如天气卡、日历卡、百科卡等几十种模态卡，在语义识别、搜索结果时效性、内容丰富性等方面更好。

目前支持的模态卡类型包括：天气、百科、医疗、万年历、火车、星座属相、贵金属、汇率、油价、手机、股票、汽车等。

以股票信息为例，网页中一般无法获取到实时的股票数据，需要结构化模态卡来支撑。博查AI Search API可以在提供网页信息的基础上，额外输出股价的结构化数据模态卡，通过模态卡提供的结构化数据，可以进一步增强AI应用中用户对于时效性问题的回答准确性。